import 'package:flutter/material.dart';
// ignore: depend_on_referenced_packages
import 'package:just_audio/just_audio.dart';
// ignore: depend_on_referenced_packages
import 'package:google_fonts/google_fonts.dart';

void main() {
  runApp(const SpotifyCloneApp());
}

class SpotifyCloneApp extends StatelessWidget {
  const SpotifyCloneApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData.dark().copyWith(
        textTheme: GoogleFonts.poppinsTextTheme(ThemeData.dark().textTheme),
        scaffoldBackgroundColor: const Color(0xFF121212),
        primaryColor: const Color(0xFF1DB954),
      ),
      debugShowCheckedModeBanner: false,
      home: const HomeScreen(),
    );
  }
}

class HomeScreen extends StatelessWidget {
  final List<Map<String, String>> playlists = const [
    {
      'title': 'Top Hits 2025',
      'image': 'https://via.placeholder.com/150',
    },
    {
      'title': 'Chill Vibes',
      'image': 'https://via.placeholder.com/150',
    },
  ];

  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Spotify Clone"),
        actions: [
          IconButton(icon: const Icon(Icons.search), onPressed: () {}),
        ],
      ),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          const Text("Playlists",
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
          const SizedBox(height: 12),
          ...playlists.map((playlist) => PlaylistCard(playlist: playlist)),
        ],
      ),
      bottomNavigationBar: BottomNavigationBar(
        backgroundColor: Colors.black,
        selectedItemColor: const Color(0xFF1DB954),
        unselectedItemColor: Colors.white,
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.home), label: 'Home'),
          BottomNavigationBarItem(icon: Icon(Icons.favorite), label: 'Favorites'),
          BottomNavigationBarItem(icon: Icon(Icons.library_music), label: 'Library'),
        ],
      ),
    );
  }
}

class PlaylistCard extends StatelessWidget {
  final Map<String, String> playlist;

  const PlaylistCard({super.key, required this.playlist});

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => Navigator.push(
        context,
        MaterialPageRoute(
          builder: (_) => MusicPlayerScreen(
            title: playlist['title']!,
            imageUrl: playlist['image']!,
            audioUrl: 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3',
          ),
        ),
      ),
      child: Container(
        margin: const EdgeInsets.symmetric(vertical: 8),
        child: Row(
          children: [
            Hero(
              tag: playlist['title']!,
              child: Image.network(
                playlist['image']!,
                width: 64,
                height: 64,
                fit: BoxFit.cover,
              ),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: Text(
                playlist['title']!,
                style: const TextStyle(fontSize: 18),
                overflow: TextOverflow.ellipsis,
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class MusicPlayerScreen extends StatefulWidget {
  final String title;
  final String audioUrl;
  final String imageUrl;

  const MusicPlayerScreen({
    super.key,
    required this.title,
    required this.audioUrl,
    required this.imageUrl,
  });

  @override
  State<MusicPlayerScreen> createState() => _MusicPlayerScreenState();
}

class _MusicPlayerScreenState extends State<MusicPlayerScreen> {
  late AudioPlayer _player;
  bool _isLoading = true;
  bool _hasError = false;

  @override
  void initState() {
    super.initState();
    _player = AudioPlayer();
    _initializePlayer();
  }

  Future<void> _initializePlayer() async {
    try {
      await _player.setUrl(widget.audioUrl);
      setState(() {
        _isLoading = false;
        _hasError = false;
      });
    } catch (e) {
      setState(() {
        _isLoading = false;
        _hasError = true;
      });
    }
  }

  @override
  void dispose() {
    _player.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(widget.title)),
      body: SafeArea(
        child: Center(
          child: _isLoading
              ? const CircularProgressIndicator()
              : _hasError
                  ? const Text('Error loading audio',
                      style: TextStyle(color: Colors.red))
                  : Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Hero(
                          tag: widget.title,
                          child: ClipRRect(
                            borderRadius: BorderRadius.circular(12),
                            child: Image.network(widget.imageUrl,
                                width: 200, height: 200, fit: BoxFit.cover),
                          ),
                        ),
                        const SizedBox(height: 20),
                        Text(widget.title,
                            style: const TextStyle(fontSize: 20)),
                        const SizedBox(height: 20),
                        StreamBuilder<PlayerState>(
                          stream: _player.playerStateStream,
                          builder: (context, snapshot) {
                            final playerState = snapshot.data;
                            final playing = playerState?.playing ?? false;
                            final processingState = playerState?.processingState;

                            if (processingState == ProcessingState.buffering) {
                              return const CircularProgressIndicator();
                            }

                            return IconButton(
                              iconSize: 64,
                              icon: Icon(
                                playing
                                    ? Icons.pause_circle
                                    : Icons.play_circle,
                              ),
                              onPressed: () {
                                if (playing) {
                                  _player.pause();
                                } else {
                                  _player.play();
                                }
                              },
                            );
                          },
                        ),
                      ],
                    ),
        ),
      ),
    );
  }
}

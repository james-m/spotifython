# some standard lib importing
#

# api.h does some win32 checking for this type so we MAY have to do something
# similar should we ever choose to support windows
#
from libc.stdint cimport uint64_t 

# at some point we'll want to allow for reading the a raw binary file.
#
cdef extern from 'appkey.h':
    ctypedef unsigned char uint8_t
    uint8_t* g_appkey
    size_t g_appkey_size

# copied from a #define in api.h, not sure if there's a better way to access
# compiler directives so we'll need to do this for now
#
DEF SPOTIFY_API_VERSION = 10
cdef extern from "libspotify/api.h":

    # common typdef structs
    #
    ctypedef struct sp_session 
    ctypedef struct sp_track 
    ctypedef struct sp_album 
    ctypedef struct sp_artist 
    ctypedef struct sp_artistbrowse 
    ctypedef struct sp_albumbrowse 
    ctypedef struct sp_toplistbrowse 
    ctypedef struct sp_search 
    ctypedef struct sp_link 
    ctypedef struct sp_image 
    ctypedef struct sp_user 
    ctypedef struct sp_playlist 
    ctypedef struct sp_playlistcontainer 
    ctypedef struct sp_inbox 
    # ERROR handling
    #
    ctypedef enum sp_error: pass
    char* sp_error_message(sp_error error)
    # copy over all the enums just in case we want to access their types in the
    # copious callbackiness of the API
    #
    ctypedef enum sp_connectionstate: pass
    ctypedef enum sp_sampletype: pass
    ctypedef struct sp_audioformat:
        sp_sampletype sample_type
        int sample_rate
        int channels
    ctypedef enum sp_bitrate: pass
    ctypedef enum sp_playlist_type: pass
    ctypedef enum sp_playlist_offline_status: pass
    ctypedef enum sp_track_availability: pass
    ctypedef enum sp_track_offline_status: 
        pass
    ctypedef struct sp_audio_buffer_stats: 
        int samples
        int stutter
    ctypedef struct sp_subscribers: 
        unsigned int count
        char *subscribers[1]
    ctypedef enum sp_connection_type: pass
    ctypedef enum sp_connection_rules: pass
    ctypedef enum sp_artistbrowse_type: pass
    ctypedef struct sp_offline_sync_status: 
        int queued_tracks
        uint64_t queued_bytes
        int done_tracks
        uint64_t done_bytes
        int copied_tracks
        uint64_t copied_bytes
        int willnotcopy_tracks
        int error_tracks
        bint syncing
    # session management
    #
    ctypedef struct sp_session_callbacks: 
        void *logged_in

    ctypedef struct sp_session_config: 
        pass

    sp_error sp_session_create(sp_session_config *config, sp_session **sess) 
    void sp_session_release(sp_session *config)
    void sp_session_login(
        sp_session *sess, char* suername, char* passowrd, bint remember_me)


    # misc. utilities
    #
    char* sp_build_id()



cimport libspotify

def get_app_key():
    result = []
    for i in range(libspotify.g_appkey_size):
        result.append(libspotify.g_appkey[i])
    return result

def get_build_id():
    return libspotify.sp_build_id()

def error_message(libspotify.sp_error err):
    return libspotify.sp_error_message(err)

def foo():
    cdef libspotify.sp_audio_buffer_stats s = libspotify.sp_audio_buffer_stats (
        samples = 10, 
        stutter = 20,
        )

    print s.samples
    

aes_key_str="""
function get_aes() {
    return key() + key() + key() + key();
}
function key() {
    return (65536 * (1 + Math.random()) | 0).toString(16).substring(1);
}

"""
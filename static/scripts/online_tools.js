function ipv4ToDecimal(ip) {
    const octets = ip.split('.').map(Number);
    if (octets.length !== 4 || octets.some(octet => octet < 0 || octet > 255)) {
        throw new Error('Invalid IPv4 address');
    }
    return (octets[0] << 24) | (octets[1] << 16) | (octets[2] << 8) | octets[3];
}

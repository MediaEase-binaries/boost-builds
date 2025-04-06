# Boost C++ Libraries Builds

Pre-built Boost C++ Libraries packages for various Linux distributions.

## 🎯 Features

- Pre-compiled binaries ready to use
- Multiple distribution support (Ubuntu & Debian)
- Automated builds via GitHub Actions
- JSON metadata for automated installations
- Both static and shared libraries included

## 🏗️ Supported Versions

### Boost Versions
- 1.69.0 to 1.88.0 (including release candidates)

### Distributions
- Debian 11 (Bullseye)
- Debian 12 (Bookworm)
- Ubuntu 22.04 (Jammy)
- Ubuntu 24.04 (Noble)

## 📋 Installation

### Manual Installation
1. Download the appropriate .deb package for your distribution from the [Releases page](https://github.com/MediaEase-binaries/boost-builds/releases)
2. Install using: `sudo dpkg -i package_name.deb`
3. Fix any dependencies if needed: `sudo apt-get install -f`

## 🔧 Build Configuration

| Feature | Configuration |
| ---     | ---           |
| Threading Support | Multi-threaded ✓ |
| C++ Standard | C++17 |
| Compiler Flags | -std=c++17 -fPIC |
| Link Type | Static + Shared |
| Runtime Link | Shared |
| Libraries | System, Python |
| Layout | System |

## 🔍 Package Details

- Each package includes:
  - Development headers
  - Static libraries (.a)
  - Shared libraries (.so)
  - Python bindings
  - CMake configuration files

- The packages are built with:
  - Full C++17 support
  - Position Independent Code (-fPIC)
  - Multi-threading support
  - System-wide installation

## 📄 Metadata

Each package is accompanied by its JSON metadata file containing:
- Package information
- Checksums
- Dependencies
- Build configuration
- Distribution details

Example metadata file:
```json
{
  "package_id": "libboost-all-dev_1.74.0",
  "version": "1.74.0",
  "build": "1build1",
  "checksum_sha256": "...",
  "build_date": "2024-03-20T12:00:00Z",
  "category": "boost",
  "tag": "stable",
  "type": "dev",
  "os": "jammy"
}
```

## 🚀 Automated Builds

- Builds are automated using GitHub Actions
- Each push to main triggers builds for all versions
- Individual versions can be built manually through the Actions tab
- Releases are automatically created and updated
- Each build is verified and tested before release


## 📝 License

Boost is distributed under the [Boost Software License](https://www.boost.org/LICENSE_1_0.txt).

## 📞 Support

If you encounter any issues or have questions:
1. Check existing [Issues](https://github.com/MediaEase-binaries/boost-builds/issues)
2. Open a new issue if needed
3. Provide as much information as possible:
   - Boost version
   - Distribution and version
   - Error messages
   - Steps to reproduce 

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zip
%global full_version 2.4.2
%global pkgname zip-2

Name:           rust-zip-2
Version:        2.4.2
Release:        %autorelease
Summary:        Rust crate "zip"
License:        MIT
URL:            https://github.com/zip-rs/zip2.git
#!RemoteAsset:  sha256:fabe6324e908f85a1c52063ce7aa26b68dcb7eb6dbc83a2d148403c9bc3eba50
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crc32fast-1/default) >= 1.4.0
Requires:       crate(displaydoc-0.2) >= 0.2.0
Requires:       crate(indexmap-2/default) >= 2.0.0
Requires:       crate(memchr-2/default) >= 2.7.0
Requires:       crate(thiserror-2/default) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/all-features) = %{version}
Provides:       crate(%{pkgname}/deflate-any) = %{version}
Provides:       crate(%{pkgname}/deflate-flate2) = %{version}
Provides:       crate(%{pkgname}/unreserved) = %{version}

%description
Source code for takopackized Rust crate "zip"

%package     -n %{name}+aes
Summary:        Support the reading and writing of zip files - feature "aes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aes-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/aes) = %{version}

%description -n %{name}+aes
This metapackage enables feature "aes" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+aes-crypto
Summary:        Support the reading and writing of zip files - feature "aes-crypto"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aes) = %{version}
Requires:       crate(%{pkgname}/constant-time-eq) = %{version}
Requires:       crate(%{pkgname}/getrandom) = %{version}
Requires:       crate(%{pkgname}/hmac) = %{version}
Requires:       crate(%{pkgname}/pbkdf2) = %{version}
Requires:       crate(%{pkgname}/sha1) = %{version}
Requires:       crate(%{pkgname}/zeroize) = %{version}
Provides:       crate(%{pkgname}/aes-crypto) = %{version}

%description -n %{name}+aes-crypto
This metapackage enables feature "aes-crypto" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bzip2
Summary:        Support the reading and writing of zip files - feature "bzip2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bzip2-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/bzip2) = %{version}

%description -n %{name}+bzip2
This metapackage enables feature "bzip2" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        Support the reading and writing of zip files - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+constant-time-eq
Summary:        Support the reading and writing of zip files - feature "constant_time_eq"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(constant-time-eq-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/constant-time-eq) = %{version}

%description -n %{name}+constant-time-eq
This metapackage enables feature "constant_time_eq" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Support the reading and writing of zip files - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aes-crypto) = %{version}
Requires:       crate(%{pkgname}/bzip2) = %{version}
Requires:       crate(%{pkgname}/deflate) = %{version}
Requires:       crate(%{pkgname}/deflate64) = %{version}
Requires:       crate(%{pkgname}/lzma) = %{version}
Requires:       crate(%{pkgname}/time) = %{version}
Requires:       crate(%{pkgname}/xz) = %{version}
Requires:       crate(%{pkgname}/zstd) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate
Summary:        Support the reading and writing of zip files - feature "deflate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/deflate-flate2) = %{version}
Requires:       crate(%{pkgname}/deflate-zopfli) = %{version}
Requires:       crate(flate2-1/rust-backend) >= 1.0.0
Provides:       crate(%{pkgname}/deflate) = %{version}

%description -n %{name}+deflate
This metapackage enables feature "deflate" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate-miniz
Summary:        Support the reading and writing of zip files - feature "deflate-miniz"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/deflate) = %{version}
Requires:       crate(%{pkgname}/deflate-flate2) = %{version}
Provides:       crate(%{pkgname}/deflate-miniz) = %{version}

%description -n %{name}+deflate-miniz
This metapackage enables feature "deflate-miniz" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate-zlib
Summary:        Support the reading and writing of zip files - feature "deflate-zlib"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/deflate-flate2) = %{version}
Requires:       crate(flate2-1/zlib) >= 1.0.0
Provides:       crate(%{pkgname}/deflate-zlib) = %{version}

%description -n %{name}+deflate-zlib
This metapackage enables feature "deflate-zlib" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate-zlib-ng
Summary:        Support the reading and writing of zip files - feature "deflate-zlib-ng"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/deflate-flate2) = %{version}
Requires:       crate(flate2-1/zlib-ng) >= 1.0.0
Provides:       crate(%{pkgname}/deflate-zlib-ng) = %{version}

%description -n %{name}+deflate-zlib-ng
This metapackage enables feature "deflate-zlib-ng" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate-zopfli
Summary:        Support the reading and writing of zip files - feature "deflate-zopfli"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/deflate-any) = %{version}
Requires:       crate(%{pkgname}/zopfli) = %{version}
Provides:       crate(%{pkgname}/deflate-zopfli) = %{version}

%description -n %{name}+deflate-zopfli
This metapackage enables feature "deflate-zopfli" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate64
Summary:        Support the reading and writing of zip files - feature "deflate64"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(deflate64-0.1/default) >= 0.1.9
Provides:       crate(%{pkgname}/deflate64) = %{version}

%description -n %{name}+deflate64
This metapackage enables feature "deflate64" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+flate2
Summary:        Support the reading and writing of zip files - feature "flate2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flate2-1) >= 1.0.0
Provides:       crate(%{pkgname}/flate2) = %{version}

%description -n %{name}+flate2
This metapackage enables feature "flate2" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Support the reading and writing of zip files - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.3/default) >= 0.3.1
Requires:       crate(getrandom-0.3/std) >= 0.3.1
Requires:       crate(getrandom-0.3/wasm-js) >= 0.3.1
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hmac
Summary:        Support the reading and writing of zip files - feature "hmac"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hmac-0.12/default) >= 0.12.0
Requires:       crate(hmac-0.12/reset) >= 0.12.0
Provides:       crate(%{pkgname}/hmac) = %{version}

%description -n %{name}+hmac
This metapackage enables feature "hmac" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lzma
Summary:        Support the reading and writing of zip files - feature "lzma"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lzma-rs-0.3/stream) >= 0.3.0
Provides:       crate(%{pkgname}/lzma) = %{version}

%description -n %{name}+lzma
This metapackage enables feature "lzma" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lzma-rs
Summary:        Support the reading and writing of zip files - feature "lzma-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lzma-rs-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/lzma-rs) = %{version}

%description -n %{name}+lzma-rs
This metapackage enables feature "lzma-rs" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nt-time
Summary:        Support the reading and writing of zip files - feature "nt-time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(nt-time-0.10) >= 0.10.6
Provides:       crate(%{pkgname}/nt-time) = %{version}

%description -n %{name}+nt-time
This metapackage enables feature "nt-time" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pbkdf2
Summary:        Support the reading and writing of zip files - feature "pbkdf2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pbkdf2-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/pbkdf2) = %{version}

%description -n %{name}+pbkdf2
This metapackage enables feature "pbkdf2" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha1
Summary:        Support the reading and writing of zip files - feature "sha1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha1-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/sha1) = %{version}

%description -n %{name}+sha1
This metapackage enables feature "sha1" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        Support the reading and writing of zip files - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3/std) >= 0.3.37
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
This metapackage enables feature "time" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xz
Summary:        Support the reading and writing of zip files - feature "xz"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(xz2-0.1/default) >= 0.1.7
Provides:       crate(%{pkgname}/xz) = %{version}

%description -n %{name}+xz
This metapackage enables feature "xz" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Support the reading and writing of zip files - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1/default) >= 1.8.0
Requires:       crate(zeroize-1/zeroize-derive) >= 1.8.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zopfli
Summary:        Support the reading and writing of zip files - feature "zopfli"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zopfli-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/zopfli) = %{version}

%description -n %{name}+zopfli
This metapackage enables feature "zopfli" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zstd
Summary:        Support the reading and writing of zip files - feature "zstd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-0.13) >= 0.13.0
Provides:       crate(%{pkgname}/zstd) = %{version}

%description -n %{name}+zstd
This metapackage enables feature "zstd" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

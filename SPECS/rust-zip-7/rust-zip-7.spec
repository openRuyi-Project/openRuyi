# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zip
%global full_version 7.2.0
%global pkgname zip-7

Name:           rust-zip-7
Version:        7.2.0
Release:        %autorelease
Summary:        Rust crate "zip"
License:        MIT
URL:            https://github.com/zip-rs/zip2.git
#!RemoteAsset:  sha256:c42e33efc22a0650c311c2ef19115ce232583abbe80850bc8b66509ebef02de0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crc32fast-1/default) >= 1.5.0
Requires:       crate(indexmap-2/default) >= 2.0.0
Requires:       crate(memchr-2/default) >= 2.7.0
Requires:       crate(typed-path-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/all-features) = %{version}
Provides:       crate(%{pkgname}/bzip2-any) = %{version}
Provides:       crate(%{pkgname}/deflate-any) = %{version}
Provides:       crate(%{pkgname}/unreserved) = %{version}

%description
Source code for takopackized Rust crate "zip"

%package     -n %{name}+arbitrary
Summary:        Support the reading and writing of zip files - feature "_arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.4.0
Requires:       crate(arbitrary-1/derive) >= 1.4.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "_arbitrary" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+aes-crypto
Summary:        Support the reading and writing of zip files - feature "aes-crypto"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aes-0.8/default) >= 0.8.0
Requires:       crate(constant-time-eq-0.3/default) >= 0.3.0
Requires:       crate(generic-array-0.14/default) >= 0.14.7
Requires:       crate(getrandom-0.3/std) >= 0.3.0
Requires:       crate(getrandom-0.3/wasm-js) >= 0.3.0
Requires:       crate(hmac-0.12/default) >= 0.12.0
Requires:       crate(hmac-0.12/reset) >= 0.12.0
Requires:       crate(pbkdf2-0.12/default) >= 0.12.0
Requires:       crate(sha1-0.10/default) >= 0.10.0
Requires:       crate(zeroize-1/default) >= 1.8.0
Requires:       crate(zeroize-1/zeroize-derive) >= 1.8.0
Provides:       crate(%{pkgname}/aes-crypto) = %{version}

%description -n %{name}+aes-crypto
This metapackage enables feature "aes-crypto" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitstream-io
Summary:        Support the reading and writing of zip files - feature "bitstream-io" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitstream-io-4/default) >= 4.5.0
Provides:       crate(%{pkgname}/bitstream-io) = %{version}
Provides:       crate(%{pkgname}/legacy-zip) = %{version}

%description -n %{name}+bitstream-io
This metapackage enables feature "bitstream-io" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "legacy-zip" feature.

%package     -n %{name}+bzip2
Summary:        Support the reading and writing of zip files - feature "bzip2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bzip2-any) = %{version}
Requires:       crate(bzip2-0.6) >= 0.6.0
Requires:       crate(bzip2-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/bzip2) = %{version}

%description -n %{name}+bzip2
This metapackage enables feature "bzip2" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bzip2-rs
Summary:        Support the reading and writing of zip files - feature "bzip2-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bzip2-any) = %{version}
Requires:       crate(bzip2-0.6) >= 0.6.0
Requires:       crate(bzip2-0.6/bzip2-sys) >= 0.6.0
Provides:       crate(%{pkgname}/bzip2-rs) = %{version}

%description -n %{name}+bzip2-rs
This metapackage enables feature "bzip2-rs" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        Support the reading and writing of zip files - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/std) >= 0.4.27
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Support the reading and writing of zip files - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aes-crypto) = %{version}
Requires:       crate(%{pkgname}/bzip2) = %{version}
Requires:       crate(%{pkgname}/deflate) = %{version}
Requires:       crate(%{pkgname}/deflate64) = %{version}
Requires:       crate(%{pkgname}/lzma) = %{version}
Requires:       crate(%{pkgname}/ppmd) = %{version}
Requires:       crate(%{pkgname}/time) = %{version}
Requires:       crate(%{pkgname}/xz) = %{version}
Requires:       crate(%{pkgname}/zstd) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate
Summary:        Support the reading and writing of zip files - feature "deflate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/deflate-flate2-zlib-rs) = %{version}
Requires:       crate(%{pkgname}/deflate-zopfli) = %{version}
Provides:       crate(%{pkgname}/deflate) = %{version}

%description -n %{name}+deflate
This metapackage enables feature "deflate" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate-flate2
Summary:        Support the reading and writing of zip files - feature "deflate-flate2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/deflate-any) = %{version}
Requires:       crate(flate2-1) >= 1.1.0
Provides:       crate(%{pkgname}/deflate-flate2) = %{version}

%description -n %{name}+deflate-flate2
This metapackage enables feature "deflate-flate2" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate-flate2-zlib
Summary:        Support the reading and writing of zip files - feature "deflate-flate2-zlib"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/deflate-flate2) = %{version}
Requires:       crate(flate2-1/zlib) >= 1.1.0
Provides:       crate(%{pkgname}/deflate-flate2-zlib) = %{version}

%description -n %{name}+deflate-flate2-zlib
This metapackage enables feature "deflate-flate2-zlib" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate-flate2-zlib-ng
Summary:        Support the reading and writing of zip files - feature "deflate-flate2-zlib-ng"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/deflate-flate2) = %{version}
Requires:       crate(flate2-1/zlib-ng) >= 1.1.0
Provides:       crate(%{pkgname}/deflate-flate2-zlib-ng) = %{version}

%description -n %{name}+deflate-flate2-zlib-ng
This metapackage enables feature "deflate-flate2-zlib-ng" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate-flate2-zlib-ng-compat
Summary:        Support the reading and writing of zip files - feature "deflate-flate2-zlib-ng-compat"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/deflate-flate2) = %{version}
Requires:       crate(flate2-1/zlib-ng-compat) >= 1.1.0
Provides:       crate(%{pkgname}/deflate-flate2-zlib-ng-compat) = %{version}

%description -n %{name}+deflate-flate2-zlib-ng-compat
This metapackage enables feature "deflate-flate2-zlib-ng-compat" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate-flate2-zlib-rs
Summary:        Support the reading and writing of zip files - feature "deflate-flate2-zlib-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/deflate-flate2) = %{version}
Requires:       crate(flate2-1/zlib-rs) >= 1.1.0
Provides:       crate(%{pkgname}/deflate-flate2-zlib-rs) = %{version}

%description -n %{name}+deflate-flate2-zlib-rs
This metapackage enables feature "deflate-flate2-zlib-rs" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate-zopfli
Summary:        Support the reading and writing of zip files - feature "deflate-zopfli"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/deflate-any) = %{version}
Requires:       crate(zopfli-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/deflate-zopfli) = %{version}

%description -n %{name}+deflate-zopfli
This metapackage enables feature "deflate-zopfli" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate64
Summary:        Support the reading and writing of zip files - feature "deflate64"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(deflate64-0.1/default) >= 0.1.10
Provides:       crate(%{pkgname}/deflate64) = %{version}

%description -n %{name}+deflate64
This metapackage enables feature "deflate64" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Support the reading and writing of zip files - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.3) >= 0.3.0
Requires:       crate(getrandom-0.3/wasm-js) >= 0.3.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+jiff-02
Summary:        Support the reading and writing of zip files - feature "jiff-02"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(jiff-0.2/default) >= 0.2.4
Provides:       crate(%{pkgname}/jiff-02) = %{version}

%description -n %{name}+jiff-02
This metapackage enables feature "jiff-02" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lzma
Summary:        Support the reading and writing of zip files - feature "lzma" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lzma-rust2-0.15/encoder) >= 0.15.0
Requires:       crate(lzma-rust2-0.15/optimization) >= 0.15.0
Requires:       crate(lzma-rust2-0.15/std) >= 0.15.0
Requires:       crate(lzma-rust2-0.15/xz) >= 0.15.0
Provides:       crate(%{pkgname}/lzma) = %{version}
Provides:       crate(%{pkgname}/xz) = %{version}

%description -n %{name}+lzma
This metapackage enables feature "lzma" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "xz" feature.

%package     -n %{name}+nt-time
Summary:        Support the reading and writing of zip files - feature "nt-time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(nt-time-0.10) >= 0.10.6
Provides:       crate(%{pkgname}/nt-time) = %{version}

%description -n %{name}+nt-time
This metapackage enables feature "nt-time" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ppmd
Summary:        Support the reading and writing of zip files - feature "ppmd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ppmd-rust-1/default) >= 1.3.0
Provides:       crate(%{pkgname}/ppmd) = %{version}

%description -n %{name}+ppmd
This metapackage enables feature "ppmd" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        Support the reading and writing of zip files - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3/std) >= 0.3.0
Requires:       crate(time-0.3/wasm-bindgen) >= 0.3.0
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
This metapackage enables feature "time" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zstd
Summary:        Support the reading and writing of zip files - feature "zstd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-0.13) >= 0.13.3
Provides:       crate(%{pkgname}/zstd) = %{version}

%description -n %{name}+zstd
This metapackage enables feature "zstd" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zip
%global full_version 0.6.6
%global pkgname zip-0.6

Name:           rust-zip-0.6
Version:        0.6.6
Release:        %autorelease
Summary:        Rust crate "zip"
License:        MIT
URL:            https://github.com/zip-rs/zip.git
#!RemoteAsset:  sha256:760394e246e4c28189f19d488c058bf16f564016aefac5d32bb1f3b51d5e9261
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-1.0/default) >= 1.4.3
Requires:       crate(crc32fast-1.0/default) >= 1.3.2
Requires:       crate(crossbeam-utils-0.8/default) >= 0.8.8
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/unreserved)

%description
Source code for takopackized Rust crate "zip"

%package     -n %{name}+aes
Summary:        Support the reading and writing of zip files - feature "aes"
Requires:       crate(%{pkgname})
Requires:       crate(aes-0.8/default) >= 0.8.2
Provides:       crate(%{pkgname}/aes)

%description -n %{name}+aes
This metapackage enables feature "aes" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+aes-crypto
Summary:        Support the reading and writing of zip files - feature "aes-crypto"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/aes)
Requires:       crate(%{pkgname}/constant-time-eq)
Requires:       crate(%{pkgname}/hmac)
Requires:       crate(%{pkgname}/pbkdf2)
Requires:       crate(%{pkgname}/sha1)
Provides:       crate(%{pkgname}/aes-crypto)

%description -n %{name}+aes-crypto
This metapackage enables feature "aes-crypto" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bzip2
Summary:        Support the reading and writing of zip files - feature "bzip2"
Requires:       crate(%{pkgname})
Requires:       crate(bzip2-0.4/default) >= 0.4.3
Provides:       crate(%{pkgname}/bzip2)

%description -n %{name}+bzip2
This metapackage enables feature "bzip2" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+constant-time-eq
Summary:        Support the reading and writing of zip files - feature "constant_time_eq"
Requires:       crate(%{pkgname})
Requires:       crate(constant-time-eq-0.1/default) >= 0.1.5
Provides:       crate(%{pkgname}/constant-time-eq)

%description -n %{name}+constant-time-eq
This metapackage enables feature "constant_time_eq" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Support the reading and writing of zip files - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/aes-crypto)
Requires:       crate(%{pkgname}/bzip2)
Requires:       crate(%{pkgname}/deflate)
Requires:       crate(%{pkgname}/time)
Requires:       crate(%{pkgname}/zstd)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate
Summary:        Support the reading and writing of zip files - feature "deflate"
Requires:       crate(%{pkgname})
Requires:       crate(flate2-1.0/rust-backend) >= 1.0.23
Provides:       crate(%{pkgname}/deflate)

%description -n %{name}+deflate
This metapackage enables feature "deflate" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate-miniz
Summary:        Support the reading and writing of zip files - feature "deflate-miniz"
Requires:       crate(%{pkgname})
Requires:       crate(flate2-1.0/default) >= 1.0.23
Provides:       crate(%{pkgname}/deflate-miniz)

%description -n %{name}+deflate-miniz
This metapackage enables feature "deflate-miniz" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate-zlib
Summary:        Support the reading and writing of zip files - feature "deflate-zlib"
Requires:       crate(%{pkgname})
Requires:       crate(flate2-1.0/zlib) >= 1.0.23
Provides:       crate(%{pkgname}/deflate-zlib)

%description -n %{name}+deflate-zlib
This metapackage enables feature "deflate-zlib" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+flate2
Summary:        Support the reading and writing of zip files - feature "flate2"
Requires:       crate(%{pkgname})
Requires:       crate(flate2-1.0) >= 1.0.23
Provides:       crate(%{pkgname}/flate2)

%description -n %{name}+flate2
This metapackage enables feature "flate2" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hmac
Summary:        Support the reading and writing of zip files - feature "hmac"
Requires:       crate(%{pkgname})
Requires:       crate(hmac-0.12/default) >= 0.12.1
Requires:       crate(hmac-0.12/reset) >= 0.12.1
Provides:       crate(%{pkgname}/hmac)

%description -n %{name}+hmac
This metapackage enables feature "hmac" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pbkdf2
Summary:        Support the reading and writing of zip files - feature "pbkdf2"
Requires:       crate(%{pkgname})
Requires:       crate(pbkdf2-0.11/default) >= 0.11.0
Provides:       crate(%{pkgname}/pbkdf2)

%description -n %{name}+pbkdf2
This metapackage enables feature "pbkdf2" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha1
Summary:        Support the reading and writing of zip files - feature "sha1"
Requires:       crate(%{pkgname})
Requires:       crate(sha1-0.10/default) >= 0.10.1
Provides:       crate(%{pkgname}/sha1)

%description -n %{name}+sha1
This metapackage enables feature "sha1" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        Support the reading and writing of zip files - feature "time"
Requires:       crate(%{pkgname})
Requires:       crate(time-0.3/std) >= 0.3.7
Provides:       crate(%{pkgname}/time)

%description -n %{name}+time
This metapackage enables feature "time" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zstd
Summary:        Support the reading and writing of zip files - feature "zstd"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-0.11/default) >= 0.11.2
Provides:       crate(%{pkgname}/zstd)

%description -n %{name}+zstd
This metapackage enables feature "zstd" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

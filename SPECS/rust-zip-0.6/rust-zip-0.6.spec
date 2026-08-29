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
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

# Drop features that depend on unpackaged crates.
Patch2000:      2000-drop-unpackaged-features.patch

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-1/default) >= 1.4.3
Requires:       crate(crc32fast-1/default) >= 1.3.2
Requires:       crate(crossbeam-utils-0.8/default) >= 0.8.8

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/unreserved) = %{version}

%description
Source code for takopackized Rust crate "zip"

%package     -n %{name}+aes
Summary:        Support the reading and writing of zip files - feature "aes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aes-0.8/default) >= 0.8.2
Provides:       crate(%{pkgname}/aes) = %{version}

%description -n %{name}+aes
This metapackage enables feature "aes" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate
Summary:        Support the reading and writing of zip files - feature "deflate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flate2-1/rust-backend) >= 1.0.23
Provides:       crate(%{pkgname}/deflate) = %{version}

%description -n %{name}+deflate
This metapackage enables feature "deflate" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate-miniz
Summary:        Support the reading and writing of zip files - feature "deflate-miniz"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flate2-1/default) >= 1.0.23
Provides:       crate(%{pkgname}/deflate-miniz) = %{version}

%description -n %{name}+deflate-miniz
This metapackage enables feature "deflate-miniz" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate-zlib
Summary:        Support the reading and writing of zip files - feature "deflate-zlib"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flate2-1/zlib) >= 1.0.23
Provides:       crate(%{pkgname}/deflate-zlib) = %{version}

%description -n %{name}+deflate-zlib
This metapackage enables feature "deflate-zlib" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+flate2
Summary:        Support the reading and writing of zip files - feature "flate2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flate2-1) >= 1.0.23
Provides:       crate(%{pkgname}/flate2) = %{version}

%description -n %{name}+flate2
This metapackage enables feature "flate2" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hmac
Summary:        Support the reading and writing of zip files - feature "hmac"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hmac-0.12/default) >= 0.12.1
Requires:       crate(hmac-0.12/reset) >= 0.12.1
Provides:       crate(%{pkgname}/hmac) = %{version}

%description -n %{name}+hmac
This metapackage enables feature "hmac" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha1
Summary:        Support the reading and writing of zip files - feature "sha1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha1-0.10/default) >= 0.10.1
Provides:       crate(%{pkgname}/sha1) = %{version}

%description -n %{name}+sha1
This metapackage enables feature "sha1" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        Support the reading and writing of zip files - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3/std) >= 0.3.7
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
This metapackage enables feature "time" for the Rust zip crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

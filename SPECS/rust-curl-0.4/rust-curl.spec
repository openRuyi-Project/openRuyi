# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name curl
%global full_version 0.4.49
%global pkgname curl-0.4

Name:           rust-curl-0.4
Version:        0.4.49
Release:        %autorelease
Summary:        Rust crate "curl"
License:        MIT
URL:            https://github.com/alexcrichton/curl-rust
#!RemoteAsset:  sha256:79fc3b6dd0b87ba36e565715bf9a2ced221311db47bd18011676f24a6066edbc
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(curl-sys-0.4) >= 0.4.87
Requires:       crate(libc-0.2/default) >= 0.2.184
Requires:       crate(schannel-0.1/default) >= 0.1.29
Requires:       crate(socket2-0.6/default) >= 0.6.3
Requires:       crate(windows-sys-0.59/default) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-foundation) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-security-cryptography) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-libraryloader) >= 0.59.0
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "curl"

%package     -n %{name}+force-system-lib-on-osx
Summary:        Rust bindings to libcurl for making HTTP requests - feature "force-system-lib-on-osx"
Requires:       crate(%{pkgname})
Requires:       crate(curl-sys-0.4/force-system-lib-on-osx) >= 0.4.87
Provides:       crate(%{pkgname}/force-system-lib-on-osx)

%description -n %{name}+force-system-lib-on-osx
This metapackage enables feature "force-system-lib-on-osx" for the Rust curl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http2
Summary:        Rust bindings to libcurl for making HTTP requests - feature "http2"
Requires:       crate(%{pkgname})
Requires:       crate(curl-sys-0.4/http2) >= 0.4.87
Provides:       crate(%{pkgname}/http2)

%description -n %{name}+http2
This metapackage enables feature "http2" for the Rust curl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mesalink
Summary:        Rust bindings to libcurl for making HTTP requests - feature "mesalink"
Requires:       crate(%{pkgname})
Requires:       crate(curl-sys-0.4/mesalink) >= 0.4.87
Provides:       crate(%{pkgname}/mesalink)

%description -n %{name}+mesalink
This metapackage enables feature "mesalink" for the Rust curl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ntlm
Summary:        Rust bindings to libcurl for making HTTP requests - feature "ntlm"
Requires:       crate(%{pkgname})
Requires:       crate(curl-sys-0.4/ntlm) >= 0.4.87
Provides:       crate(%{pkgname}/ntlm)

%description -n %{name}+ntlm
This metapackage enables feature "ntlm" for the Rust curl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+openssl-probe
Summary:        Rust bindings to libcurl for making HTTP requests - feature "openssl-probe"
Requires:       crate(%{pkgname})
Requires:       crate(openssl-probe-0.1/default) >= 0.1.6
Provides:       crate(%{pkgname}/openssl-probe)

%description -n %{name}+openssl-probe
This metapackage enables feature "openssl-probe" for the Rust curl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+openssl-sys
Summary:        Rust bindings to libcurl for making HTTP requests - feature "openssl-sys"
Requires:       crate(%{pkgname})
Requires:       crate(openssl-sys-0.9/default) >= 0.9.112
Provides:       crate(%{pkgname}/openssl-sys)

%description -n %{name}+openssl-sys
This metapackage enables feature "openssl-sys" for the Rust curl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+poll-7-68-0
Summary:        Rust bindings to libcurl for making HTTP requests - feature "poll_7_68_0"
Requires:       crate(%{pkgname})
Requires:       crate(curl-sys-0.4/poll-7-68-0) >= 0.4.87
Provides:       crate(%{pkgname}/poll-7-68-0)

%description -n %{name}+poll-7-68-0
This metapackage enables feature "poll_7_68_0" for the Rust curl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+protocol-ftp
Summary:        Rust bindings to libcurl for making HTTP requests - feature "protocol-ftp"
Requires:       crate(%{pkgname})
Requires:       crate(curl-sys-0.4/protocol-ftp) >= 0.4.87
Provides:       crate(%{pkgname}/protocol-ftp)

%description -n %{name}+protocol-ftp
This metapackage enables feature "protocol-ftp" for the Rust curl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls
Summary:        Rust bindings to libcurl for making HTTP requests - feature "rustls"
Requires:       crate(%{pkgname})
Requires:       crate(curl-sys-0.4/rustls) >= 0.4.87
Provides:       crate(%{pkgname}/rustls)

%description -n %{name}+rustls
This metapackage enables feature "rustls" for the Rust curl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+spnego
Summary:        Rust bindings to libcurl for making HTTP requests - feature "spnego"
Requires:       crate(%{pkgname})
Requires:       crate(curl-sys-0.4/spnego) >= 0.4.87
Provides:       crate(%{pkgname}/spnego)

%description -n %{name}+spnego
This metapackage enables feature "spnego" for the Rust curl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ssl
Summary:        Rust bindings to libcurl for making HTTP requests - feature "ssl" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/openssl-probe)
Requires:       crate(%{pkgname}/openssl-sys)
Requires:       crate(curl-sys-0.4/ssl) >= 0.4.87
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/ssl)

%description -n %{name}+ssl
This metapackage enables feature "ssl" for the Rust curl crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+static-curl
Summary:        Rust bindings to libcurl for making HTTP requests - feature "static-curl"
Requires:       crate(%{pkgname})
Requires:       crate(curl-sys-0.4/static-curl) >= 0.4.87
Provides:       crate(%{pkgname}/static-curl)

%description -n %{name}+static-curl
This metapackage enables feature "static-curl" for the Rust curl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+static-ssl
Summary:        Rust bindings to libcurl for making HTTP requests - feature "static-ssl"
Requires:       crate(%{pkgname})
Requires:       crate(curl-sys-0.4/static-ssl) >= 0.4.87
Provides:       crate(%{pkgname}/static-ssl)

%description -n %{name}+static-ssl
This metapackage enables feature "static-ssl" for the Rust curl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+upkeep-7-62-0
Summary:        Rust bindings to libcurl for making HTTP requests - feature "upkeep_7_62_0"
Requires:       crate(%{pkgname})
Requires:       crate(curl-sys-0.4/upkeep-7-62-0) >= 0.4.87
Provides:       crate(%{pkgname}/upkeep-7-62-0)

%description -n %{name}+upkeep-7-62-0
This metapackage enables feature "upkeep_7_62_0" for the Rust curl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+windows-static-ssl
Summary:        Rust bindings to libcurl for making HTTP requests - feature "windows-static-ssl"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/static-curl)
Requires:       crate(curl-sys-0.4/windows-static-ssl) >= 0.4.87
Provides:       crate(%{pkgname}/windows-static-ssl)

%description -n %{name}+windows-static-ssl
This metapackage enables feature "windows-static-ssl" for the Rust curl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zlib-ng-compat
Summary:        Rust bindings to libcurl for making HTTP requests - feature "zlib-ng-compat"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/static-curl)
Requires:       crate(curl-sys-0.4/zlib-ng-compat) >= 0.4.87
Provides:       crate(%{pkgname}/zlib-ng-compat)

%description -n %{name}+zlib-ng-compat
This metapackage enables feature "zlib-ng-compat" for the Rust curl crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

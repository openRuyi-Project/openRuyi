# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name curl-sys
%global full_version 0.4.87+curl-8.19.0
%global pkgname curl-sys-0.4

Name:           rust-curl-sys-0.4
Version:        0.4.87
Release:        %autorelease
Summary:        Rust crate "curl-sys"
License:        MIT
URL:            https://github.com/alexcrichton/curl-rust
#!RemoteAsset:  sha256:61a460380f0ef783703dcbe909107f39c162adeac050d73c850055118b5b6327
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1.0/default) >= 1.2.58
Requires:       crate(libc-0.2/default) >= 0.2.184
Requires:       crate(libz-sys-1.0/libc) >= 1.1.25
Requires:       crate(pkg-config-0.3/default) >= 0.3.32
Requires:       crate(vcpkg-0.2/default) >= 0.2.15
Requires:       crate(windows-sys-0.59/default) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-networking-winsock) >= 0.59.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/force-system-lib-on-osx)
Provides:       crate(%{pkgname}/mesalink)
Provides:       crate(%{pkgname}/ntlm)
Provides:       crate(%{pkgname}/poll-7-68-0)
Provides:       crate(%{pkgname}/protocol-ftp)
Provides:       crate(%{pkgname}/spnego)
Provides:       crate(%{pkgname}/static-curl)
Provides:       crate(%{pkgname}/upkeep-7-62-0)
Provides:       crate(%{pkgname}/windows-static-ssl)

%description
Source code for takopackized Rust crate "curl-sys"

%package     -n %{name}+libnghttp2-sys
Summary:        Native bindings to the libcurl library - feature "libnghttp2-sys" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(libnghttp2-sys-0.1/default) >= 0.1.13
Provides:       crate(%{pkgname}/http2)
Provides:       crate(%{pkgname}/libnghttp2-sys)

%description -n %{name}+libnghttp2-sys
This metapackage enables feature "libnghttp2-sys" for the Rust curl-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "http2" feature.

%package     -n %{name}+openssl-sys
Summary:        Native bindings to the libcurl library - feature "openssl-sys" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(openssl-sys-0.9/default) >= 0.9.112
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/openssl-sys)
Provides:       crate(%{pkgname}/ssl)

%description -n %{name}+openssl-sys
This metapackage enables feature "openssl-sys" for the Rust curl-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "ssl" features.

%package     -n %{name}+rustls-ffi
Summary:        Native bindings to the libcurl library - feature "rustls-ffi" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(rustls-ffi-0.15/default) >= 0.15.0
Requires:       crate(rustls-ffi-0.15/no-log-capture) >= 0.15.0
Provides:       crate(%{pkgname}/rustls)
Provides:       crate(%{pkgname}/rustls-ffi)

%description -n %{name}+rustls-ffi
This metapackage enables feature "rustls-ffi" for the Rust curl-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rustls" feature.

%package     -n %{name}+static-ssl
Summary:        Native bindings to the libcurl library - feature "static-ssl"
Requires:       crate(%{pkgname})
Requires:       crate(openssl-sys-0.9/vendored) >= 0.9.112
Provides:       crate(%{pkgname}/static-ssl)

%description -n %{name}+static-ssl
This metapackage enables feature "static-ssl" for the Rust curl-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zlib-ng-compat
Summary:        Native bindings to the libcurl library - feature "zlib-ng-compat"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/static-curl)
Requires:       crate(libz-sys-1.0/libc) >= 1.1.25
Requires:       crate(libz-sys-1.0/zlib-ng) >= 1.1.25
Provides:       crate(%{pkgname}/zlib-ng-compat)

%description -n %{name}+zlib-ng-compat
This metapackage enables feature "zlib-ng-compat" for the Rust curl-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

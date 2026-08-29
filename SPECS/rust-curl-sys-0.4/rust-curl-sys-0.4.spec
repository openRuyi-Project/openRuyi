# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
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
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.2
Requires:       crate(libz-sys-1/libc) >= 1.0.18
Requires:       crate(pkg-config-0.3) >= 0.3.3
Requires:       crate(windows-sys-0.59/default) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-networking-winsock) >= 0.59.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/force-system-lib-on-osx) = %{version}
Provides:       crate(%{pkgname}/mesalink) = %{version}
Provides:       crate(%{pkgname}/ntlm) = %{version}
Provides:       crate(%{pkgname}/poll-7-68-0) = %{version}
Provides:       crate(%{pkgname}/protocol-ftp) = %{version}
Provides:       crate(%{pkgname}/spnego) = %{version}
Provides:       crate(%{pkgname}/static-curl) = %{version}
Provides:       crate(%{pkgname}/upkeep-7-62-0) = %{version}
Provides:       crate(%{pkgname}/windows-static-ssl) = %{version}

%description
Source code for takopackized Rust crate "curl-sys"

%package     -n %{name}+libnghttp2-sys
Summary:        Native bindings to the libcurl library - feature "libnghttp2-sys" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libnghttp2-sys-0.1/default) >= 0.1.3
Provides:       crate(%{pkgname}/http2) = %{version}
Provides:       crate(%{pkgname}/libnghttp2-sys) = %{version}

%description -n %{name}+libnghttp2-sys
This metapackage enables feature "libnghttp2-sys" for the Rust curl-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "http2" feature.

%package     -n %{name}+openssl-sys
Summary:        Native bindings to the libcurl library - feature "openssl-sys" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(openssl-sys-0.9/default) >= 0.9.64
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/openssl-sys) = %{version}
Provides:       crate(%{pkgname}/ssl) = %{version}

%description -n %{name}+openssl-sys
This metapackage enables feature "openssl-sys" for the Rust curl-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "ssl" features.

%package     -n %{name}+rustls-ffi
Summary:        Native bindings to the libcurl library - feature "rustls-ffi" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-ffi-0.15/default) >= 0.15.0
Requires:       crate(rustls-ffi-0.15/no-log-capture) >= 0.15.0
Provides:       crate(%{pkgname}/rustls) = %{version}
Provides:       crate(%{pkgname}/rustls-ffi) = %{version}

%description -n %{name}+rustls-ffi
This metapackage enables feature "rustls-ffi" for the Rust curl-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rustls" feature.

%package     -n %{name}+static-ssl
Summary:        Native bindings to the libcurl library - feature "static-ssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(openssl-sys-0.9/vendored) >= 0.9.64
Provides:       crate(%{pkgname}/static-ssl) = %{version}

%description -n %{name}+static-ssl
This metapackage enables feature "static-ssl" for the Rust curl-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zlib-ng-compat
Summary:        Native bindings to the libcurl library - feature "zlib-ng-compat"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/static-curl) = %{version}
Requires:       crate(libz-sys-1/libc) >= 1.0.18
Requires:       crate(libz-sys-1/zlib-ng) >= 1.0.18
Provides:       crate(%{pkgname}/zlib-ng-compat) = %{version}

%description -n %{name}+zlib-ng-compat
This metapackage enables feature "zlib-ng-compat" for the Rust curl-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

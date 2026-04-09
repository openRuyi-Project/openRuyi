# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           curl-impersonate-chrome
Version:        0.7.0
Release:        %autorelease
Summary:        curl with browser impersonation capabilities
License:        MIT
URL:            https://github.com/lexiforest/curl-impersonate
#!RemoteAsset
Source0:        %{url}/archive/v%{version}.tar.gz
# vendor sources, patched version of which are needed for this package
#!RemoteAsset
Source1:        https://github.com/google/boringssl/archive/d24a38200fef19150eef00cad35b138936c08767.zip#/boringssl-d24a38200fef19150eef00cad35b138936c08767.zip
#!RemoteAsset
Source2:        https://github.com/curl/curl/archive/curl-8_7_1.tar.gz
BuildSystem:    autotools

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake >= 3.5
BuildRequires:  ninja
BuildRequires:  golang
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  unzip
# Use system libraries for brotli, nghttp2, zlib, zstd
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libnghttp2)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libzstd)

Requires:       brotli
Requires:       nghttp2
Requires:       zlib
Requires:       libzstd

%patchlist
# Fix installation path to respect DESTDIR for RPM packaging
0001-install-sh-scripts-to-buildroot.patch
# Use system brotli and nghttp2 libraries instead of building from source
0002-use-system-brotli-nghttp2-skip-downloads.patch
# Remove -Werror flag from BoringSSL build to avoid compilation failures
0003-remove-werror-in-boringssl-build.patch
# Respect LIBDIR variable
0004-force-curl-install-to-libdir.patch

%description
A special build of curl that can impersonate Chrome, Edge, Safari and Firefox.
curl-impersonate performs TLS and HTTP handshakes identical to real browsers.

This package includes support for:
- Chrome/Edge browser impersonation
- Safari browser impersonation
- HTTP/2 support
- BoringSSL (Google's TLS library, statically compiled)
- Brotli compression (using system library)

BoringSSL is statically compiled and bundled.
Other dependencies (brotli, nghttp2, zlib, zstd) use system packages.

%build
# Build using pre-downloaded sources (no network access needed)
# brotli and nghttp2 will use system libraries
cp %{SOURCE1} boringssl.zip
cp %{SOURCE2} curl-8_7_1.tar.gz
%__make chrome-build

%install
%__make DESTDIR=%{buildroot} chrome-install

%check
# Verify the build includes all required features
%__make chrome-checkbuild

%files
%license LICENSE
%doc README.md INSTALL.md
%{_bindir}/curl_*
%{_bindir}/%{name}
%{_bindir}/%{name}-config
%{_libdir}/libcurl-impersonate-chrome.so*
# it do need bundle the static lib, used for
%{_libdir}/libcurl-impersonate-chrome.a*

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fuse2
Version:        2.9.9
Release:        %autorelease
Summary:        FUSE 2 compatibility libraries
License:        LGPL-2.1-only AND GPL-2.0-only
URL:            https://github.com/libfuse/libfuse
VCS:            git:https://github.com/libfuse/libfuse.git
#!RemoteAsset:  sha256:d0e69d5d608cc22ff4843791ad097f554dd32540ddc9bed7638cc6fea7c1b4b5
Source0:        https://github.com/libfuse/libfuse/releases/download/fuse-%{version}/fuse-%{version}.tar.gz
BuildSystem:    autotools

# Backport upstream glibc 2.34 closefrom detection (Sam James).
# https://github.com/libfuse/libfuse/commit/5a43d0f724c56f8836f3f92411e0de1b5f82db32
Patch0001:      0001-conditionally-define-closefrom.patch

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-util
BuildOption(conf):  --disable-example
BuildOption(conf):  --disable-mtab

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  fuse3
# fuse3 owns the unversioned fusermount and the shared configuration.
Requires:       fuse3

%description
Compatibility libraries for applications using the FUSE 2 API, including
libfuse and libulockmgr. Mounting uses the fusermount helper supplied by
fuse3, allowing both library versions to be installed together.

%package        devel
Summary:        Development files for the FUSE 2 API
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
Headers and linker files for building applications against FUSE 2.

%prep
%autosetup -p1 -n fuse-%{version}
# Regenerate configure and config.h.in for upstream closefrom detection.
# AM_ICONV is shipped by gettext-tools in the standard build environment.
autoreconf -fi -I %{_datadir}/gettext/m4

%build -a
# Build only the lock manager helper; do not build the old mount helpers.
%make_build -C util ulockmgr_server
%make_build -C example hello

%install -a
install -D -m 0755 util/ulockmgr_server %{buildroot}%{_bindir}/ulockmgr_server
# The mount helpers and their manual pages belong to fuse3.
rm -f %{buildroot}%{_mandir}/man1/fusermount.1*
rm -f %{buildroot}%{_mandir}/man8/mount.fuse.8*

%check
# The upstream example exits 1 after displaying --version (no mount).
# Check both the FUSE 2 library and the FUSE 3 helper it actually invoked.
status=0
output=$(LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./example/.libs/hello --version 2>&1) || status=$?
test "$status" -eq 1
printf '%s\n' "$output"
printf '%s\n' "$output" | grep -F 'FUSE library version: %{version}'
printf '%s\n' "$output" | grep -F 'fusermount3 version:'

%files
%doc AUTHORS ChangeLog NEWS README.md
%license COPYING COPYING.LIB
%{_libdir}/libfuse.so.*
%{_libdir}/libulockmgr.so.*
%{_bindir}/ulockmgr_server
%{_mandir}/man1/ulockmgr_server.1*

%files devel
%{_includedir}/fuse.h
%{_includedir}/fuse/
%{_includedir}/ulockmgr.h
%{_libdir}/libfuse.so
%{_libdir}/libulockmgr.so
%{_libdir}/pkgconfig/fuse.pc

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cdparanoia
Version:        10.2
Release:        %autorelease
Summary:        Compact Disc Digital Audio (CDDA) extraction tool (or ripper)
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.xiph.org/paranoia/index.html
# No VCS link available
#!RemoteAsset
Source0:        https://downloads.xiph.org/releases/cdparanoia/cdparanoia-III-%{version}.src.tgz
BuildSystem:    autotools

BuildOption(build):  OPT="%{optflags} -Wno-pointer-sign -Wno-unused"
BuildOption(build):  LDFLAGS="%{?build_ldflags}"
# -flto induced parallel build errors
BuildOption(build):  -j1

BuildRequires:  config
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make

%description
Cdparanoia (Paranoia III) reads digital audio directly from a CD, then
writes the data to a file or pipe in WAV, AIFC or raw 16 bit linear
PCM format.  Cdparanoia doesn't contain any extra features (like the ones
included in the cdda2wav sampling utility).  Instead, cdparanoia's strength
lies in its ability to handle a variety of hardware, including inexpensive
drives prone to misalignment, frame jitter and loss of streaming during
atomic reads.  Cdparanoia is also good at reading and repairing data from
damaged CDs.

%package        devel
Summary:        Development tools for libcdda_paranoia (Paranoia III)
Requires:       %{name}%{?_isa} = %{version}-%{release}

License:        LGPL-2.1-or-later

%patchlist
# Rename private to private_data
cdparanoia-10.2-#463009.patch
# Fix null pointer dereference in cdda_read_timed
cdparanoia-10.2-endian.patch
# Use DESTDIR in install Makefile rule
cdparanoia-10.2-install.patch
# main: fix format-security warning
cdparanoia-10.2-format-security.patch
# Remove redundant configure.guess/configure.sub copy in build scripts
cdparanoia-use-proper-gnu-config-files.patch
# Pass LDFLAGS when linking shared libraries
cdparanoia-10.2-ldflags.patch
# Add pkg-config support via cdparanoia-3.pc
cdparanoia-10.2-add-pkgconfig.patch

%description    devel
The cdparanoia-devel package contains the libraries and header files needed
for developing applications to read CD Digital Audio disks.

%conf
autoreconf -ifv
# BuildOption(conf) adds --docdir by default, which is not supported here.
# Use %configure directly to avoid configure errors.
%configure --includedir=%{_includedir}/cdda

# No check
%check

%install -a
rm -f %{buildroot}%{_libdir}/*.a

%files
%doc COPYING* README
%{_bindir}/cdparanoia
%{_mandir}/man1/cdparanoia.1*
%{_libdir}/*.so.*

%files devel
%{_includedir}/cdda/
%{_libdir}/pkgconfig/cdparanoia-3.pc
%{_libdir}/*.so

%changelog
%{?autochangelog}

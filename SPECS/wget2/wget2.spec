# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond as_wget 1

Name:           wget2
Version:        2.2.0
Release:        %autorelease
Summary:        An advanced file and recursive website downloader
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND GFDL-1.3-or-later
URL:            https://gitlab.com/gnuwget/wget2
#!RemoteAsset
Source:         https://ftp.gnu.org/gnu/wget/wget2-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf): --disable-static

BuildRequires:  autoconf automake libtool flex-devel gettext >= 0.18.2 gcc make

BuildRequires:  bzip2-devel python3 texinfo
BuildRequires:  pkgconfig(gnutls) pkgconfig(gpgme) pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libidn2)  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libmicrohttpd) pkgconfig(libnghttp2)
BuildRequires:  pcre2-devel pkgconfig(libpsl) pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)

Provides:       webclient
Requires:       %{name}-libs = %{version}

%description
GNU Wget2 is the successor of GNU Wget, a file and recursive website downloader,
designed to be faster and more feature-rich.

%package        libs
Summary:        Runtime libraries for GNU Wget2
Provides:       bundled(gnulib)

%description    libs
This package contains the shared libraries for applications to use Wget2 functionality.

%package        devel
Summary:        Libraries and header files for using wget2 libraries
Requires:       %{name}-libs = %{version}

%description   devel
Development libraries and headers for building applications that use GNU Wget2.

%if %{with as_wget}
%package        wget
Summary:        A compatibility shim to provide wget via wget2
Requires:       wget2 = %{version}
Conflicts:      wget < 2
Provides:       wget = %{version}
Provides:       wget%{?_isa} = %{version}
Provides:       webclient

%description    wget
This package provides symbolic links for wget2 to be used in place of the original wget.
%endif

%install -a
rm -f %{buildroot}%{_bindir}/%{name}_noinstall
%find_lang %{name} --generate-subpackages
%if %{with as_wget}
ln -sr %{buildroot}%{_bindir}/wget2 %{buildroot}%{_bindir}/wget
%endif

# XXX: fix tests.
%check

%files
%license COPYING*
%doc README.md
%{_bindir}/wget2

%files libs
%license COPYING*
%{_libdir}/libwget*.so.*

%files devel
%{_includedir}/wget.h
%{_includedir}/wgetver.h
%{_libdir}/libwget*.so
%{_libdir}/pkgconfig/libwget.pc

%if %{with as_wget}
%files wget
%{_bindir}/wget
%endif

%changelog
%{?autochangelog}

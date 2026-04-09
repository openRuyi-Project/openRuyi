# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond as_wget 1

Name:           wget2
Version:        2.2.1
Release:        %autorelease
Summary:        An advanced file and recursive website downloader
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND GFDL-1.3-or-later
URL:            https://gitlab.com/gnuwget/wget2
#!RemoteAsset:  sha256:d7544b13e37f18e601244fce5f5f40688ac1d6ab9541e0fbb01a32ee1fb447b4
Source:         https://ftpmirror.gnu.org/gnu/wget/wget2-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  flex-devel
BuildRequires:  gettext
BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  bzip2-devel
BuildRequires:  python3
BuildRequires:  texinfo
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libidn2)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libmicrohttpd)
BuildRequires:  pkgconfig(libnghttp2)
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig(libpsl)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)

Provides:       webclient
Requires:       %{name}-libs = %{version}-%{release}

%description
GNU Wget2 is the successor of GNU Wget, a file and recursive website downloader,
designed to be faster and more feature-rich.

%package        libs
Summary:        Runtime libraries for GNU Wget2

%description    libs
This package contains the shared libraries for applications to use Wget2 functionality.

%package        devel
Summary:        Libraries and header files for using wget2 libraries
Requires:       %{name}-libs = %{version}-%{release}

%description   devel
Development libraries and headers for building applications that use GNU Wget2.

%if %{with as_wget}
%package        wget
Summary:        A compatibility shim to provide wget via wget2
Requires:       wget2 = %{version}-%{release}
Conflicts:      wget < 2
Provides:       wget = %{version}-%{release}
Provides:       wget%{?_isa} = %{version}-%{release}
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
%autochangelog

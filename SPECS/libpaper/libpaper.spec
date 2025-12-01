# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libpaper
Version:        2.2.6
Release:        %autorelease
Summary:        Library and tools for handling papersize
License:        LGPL-2.1-or-later AND LicenseRef-openRuyi-Public-Domain AND GPL-3.0-or-later AND LGPL-2.0-or-later AND FSFAP
URL:            https://github.com/rrthomas/libpaper/
#!RemoteAsset
Source0:        https://github.com/rrthomas/libpaper/releases/download/v%{version}/libpaper-%{version}.tar.gz
# Pulled from paper
Source1:        localepaper.c
# from libpaper-1.x
Source2:        paperconf
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  gettext
BuildRequires:  gawk
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  help2man
BuildRequires:  tar
BuildRequires:  perl
BuildRequires:  gzip

Provides:       bundled(gnulib)

%description
The libpaper package enables users to indicate their preferred paper
size and specifies system-wide and per-user paper size catalogues, which can
also be used directly (see paperspecs(5)).

%package        devel
Summary:        Headers/Libraries for developing programs that use libpaper
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains headers and libraries that programmers will need
to develop applications which use libpaper.

%package     -n paper
Summary:        Print paper size information
Requires:       %{name} = %{version}-%{release}
License:        GPL-3.0-or-later AND FSFAP AND GPL-2.0-only

%description -n paper
The paper(1) utility can be used to find the user's preferred
default paper size and give information about known sizes.

%prep -a
cp %{SOURCE1} src/

%build -a
# localepaper
pushd src
%{__cc} %{optflags} -I.. -Ilibgnu -o localepaper localepaper.c libgnu/.libs/libgnupaper.a
popd

%install -a
rm -rf %{buildroot}%{_datadir}/doc/libpaper/README.md
rm $RPM_BUILD_ROOT%{_libdir}/*.la
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}

mkdir %{buildroot}%{_libexecdir}
install -m0755 src/localepaper %{buildroot}%{_libexecdir}

gzip -c %{SOURCE2} > paperconf.1.gz
install -m0644 paperconf.1.gz %{buildroot}%{_mandir}/man1/paperconf.1

%files
%doc ChangeLog README
%license COPYING
%config(noreplace) %{_sysconfdir}/paperspecs
%{_libdir}/libpaper.so.2*

%files devel
%{_includedir}/paper.h
%{_libdir}/libpaper.so

%files -n paper
%{_bindir}/paper
%{_bindir}/paperconf
%{_libexecdir}/localepaper
%{_mandir}/man1/paper.*
%{_mandir}/man1/paperconf.*
%{_mandir}/man5/paperspecs.*

%changelog
%{?autochangelog}

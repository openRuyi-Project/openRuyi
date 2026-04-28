# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:            libisoburn
Version:         1.5.6
Release:         %autorelease
Summary:         Library for creating and expanding ISO-9660 filesystems
License:         GPL-2.0-or-later
URL:             https://libburnia-project.org/
VCS:             git:https://dev.lovelyhq.com/libburnia/libisoburn.git
#!RemoteAsset
Source0:         https://files.libburnia-project.org/releases/libisoburn-%{version}.tar.gz
Source1:         xorriso_extract_iso_image.desktop
BuildSystem:     autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-doxygen-docs

BuildRequires:   gcc
BuildRequires:   gcc-c++
BuildRequires:   make
BuildRequires:   pkgconfig(readline)
BuildRequires:   pkgconfig(libacl)
BuildRequires:   pkgconfig(zlib)
BuildRequires:   pkgconfig(libburn-1) >= %{version}
BuildRequires:   pkgconfig(libisofs-1) >= %{version}
BuildRequires:   autoconf
BuildRequires:   automake
BuildRequires:   libtool

%description
Libisoburn is a frontend for libburn and libisofs, enabling creation and expansion
of ISO-9660 filesystems on all optical media.

%package         devel
Summary:         Development files for %{name}
Requires:        %{name}%{?_isa} = %{version}-%{release}
Requires:        pkgconfig

%description     devel
This package contains libraries and header files for developing applications
that use libisoburn.

%package     -n  xorriso
Summary:         ISO-9660 and Rock Ridge image manipulation tool
URL:             https://scdbackup.sourceforge.net/xorriso_eng.html
Requires:        %{name}%{?_isa} = %{version}-%{release}
Requires(post):  alternatives
Requires(preun): alternatives

%description -n xorriso
Xorriso copies file objects into Rock Ridge enhanced ISO-9660 filesystems and
allows session-wise manipulation of such filesystems.

%conf -p
autoreconf -fiv

%install -a
rm -f %{buildroot}%{_bindir}/xorriso-tcltk*
touch %{buildroot}%{_bindir}/cdrecord
touch %{buildroot}%{_bindir}/mkisofs
touch %{buildroot}%{_mandir}/man1/cdrecord.1.gz
touch %{buildroot}%{_mandir}/man1/mkisofs.1.gz

%post -n xorriso
alternatives --install %{_bindir}/cdrecord cdrecord %{_bindir}/xorrecord 50 \
  --slave %{_mandir}/man1/cdrecord.1.gz cdrecord-man %{_mandir}/man1/xorrecord.1.gz
alternatives --install %{_bindir}/mkisofs mkisofs %{_bindir}/xorrisofs 50 \
  --slave %{_mandir}/man1/mkisofs.1.gz mkisofs-man %{_mandir}/man1/xorrisofs.1.gz

%preun -n xorriso
if [ $1 -eq 0 ]; then
  alternatives --remove cdrecord %{_bindir}/xorrecord
  alternatives --remove mkisofs %{_bindir}/xorrisofs
fi

%files
%license COPYING
%doc AUTHORS COPYRIGHT README ChangeLog
%{_libdir}/libisoburn*.so.*

%files devel
%{_includedir}/libisoburn
%{_libdir}/libisoburn.so
%{_libdir}/pkgconfig/libisoburn-1.pc

%files -n xorriso
%ghost %{_bindir}/cdrecord
%ghost %{_bindir}/mkisofs
%{_bindir}/osirrox
%{_bindir}/xorrecord
%{_bindir}/xorriso
%{_bindir}/xorrisofs
%{_bindir}/xorriso-dd-target
%{_mandir}/man1/*.1*
%{_infodir}/*.info*

%changelog
%{?autochangelog}

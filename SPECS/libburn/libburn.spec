# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:            libburn
Version:         1.5.6
Release:         %autorelease
Summary:         Library for reading, mastering and writing optical discs
License:         GPL-2.0-or-later
URL:             https://libburnia-project.org/
#!RemoteAsset
Source:          https://files.libburnia-project.org/releases/libburn-%{version}.tar.gz
Patch:           0001-libburn-1.5.6-c23.patch
BuildSystem:     autotools

BuildOption(conf): --disable-static
BuildOption(conf): --disable-doxygen-docs
BuildOption(build): CFLAGS="%{optflags} -Wno-error=format-overflow"

BuildRequires:   gcc make intltool gettext autoconf automake libtool

Requires(post):  update-alternatives
Requires(preun): update-alternatives

%description
Libburn is a library for writing and reading data to/from optical media like
CD, DVD, and Blu-Ray discs.

%package         devel
Summary:         Development files for %{name}
Requires:        %{name} = %{version}
Requires:        pkgconfig

%description     devel
This package contains the libraries, header files, API documentation, and
tools needed to develop applications that use libburn.

%conf -p
autoreconf -fiv

%install -a
touch %{buildroot}%{_bindir}/cdrecord
touch %{buildroot}%{_mandir}/man1/cdrecord.1.gz

%post
/usr/sbin/alternatives --install %{_bindir}/cdrecord cdrecord %{_bindir}/cdrskin 50 \
  --slave %{_mandir}/man1/cdrecord.1.gz cdrecord-man %{_mandir}/man1/cdrskin.1.gz

%preun
if [ $1 -eq 0 ]; then
  /usr/sbin/alternatives --remove cdrecord %{_bindir}/cdrskin
fi

%files
%license COPYING
%doc AUTHORS COPYRIGHT README
%{_libdir}/libburn*.so.*
%{_bindir}/cdrskin
%ghost %{_bindir}/cdrecord
%{_mandir}/man1/cdrskin.1*
%ghost %{_mandir}/man1/cdrecord.1*

%files devel
%{_includedir}/libburn
%{_libdir}/libburn*.so
%{_libdir}/pkgconfig/libburn*.pc

%changelog
%{?autochangelog}

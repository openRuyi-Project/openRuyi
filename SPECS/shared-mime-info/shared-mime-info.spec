# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           shared-mime-info
Version:        2.4
Release:        %autorelease
Summary:        Shared MIME information database
License:        GPL-2.0-or-later
URL:            http://freedesktop.org/Software/shared-mime-info
#!RemoteAsset
Source0:        https://gitlab.freedesktop.org/xdg/shared-mime-info/-/archive/%{version}/shared-mime-info-%{version}.tar.gz
# Work-around for https://bugs.freedesktop.org/show_bug.cgi?id=40354
Patch0001:      0001-Remove-sub-classing-from-OO.o-mime-types.patch
# Fix build with libxml2 2.12.0
# https://gitlab.freedesktop.org/xdg/shared-mime-info/-/issues/219
Patch0002:      0002-Fix-build-with-libxml2-2.12.0.patch

BuildSystem:    meson

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  perl-XML-Parser
BuildRequires:  meson
BuildRequires:  itstool
BuildRequires:  xmlto
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.6.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.4
BuildRequires:  docbook-xsl
BuildRequires:  docbook-dtds

%global __requires_exclude ^/usr/bin/pkg-config$

%description
The shared-mime-info package contains the core database of common types
and the update-mime-database command used to extend it. It requires
glib2 to be installed for building the update command. Additionally, it
uses intltool for translations, though this is only a dependency for
the maintainers.

%install -a
find %{buildroot}%{_datadir}/mime -type d \
| sed -e "s|^%{buildroot}|%%dir |" > %{name}.files
find %{buildroot}%{_datadir}/mime -type f -not -path "*/packages/*" \
| sed -e "s|^%{buildroot}|%%ghost |" >> %{name}.files

# remove bogus translation files
# translations are already in the xml file installed
rm -rf %{buildroot}%{_datadir}/locale/*

%check
%meson_test

%post
/bin/touch --no-create %{_datadir}/mime/packages &>/dev/null ||:

%transfiletriggerin -- %{_datadir}/mime
update-mime-database -n %{_datadir}/mime &> /dev/null ||:

%transfiletriggerpostun -- %{_datadir}/mime
update-mime-database -n %{_datadir}/mime &> /dev/null ||:

%files
%license COPYING
%doc README.md NEWS HACKING.md data/shared-mime-info-spec.xml
%{_bindir}/update-mime-database
%{_datadir}/mime/packages/*.org.xml
%dir %{_datadir}/pkgconfig
%{_datadir}/pkgconfig/shared-mime-info.pc
%dir %{_datadir}/gettext
%dir %{_datadir}/gettext/its
%{_datadir}/gettext/its/shared-mime-info.its
%{_datadir}/gettext/its/shared-mime-info.loc
%{_mandir}/man1/*

%changelog
%{?autochangelog}

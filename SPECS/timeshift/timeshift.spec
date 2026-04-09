# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           timeshift
Version:        25.12.4
Release:        %autorelease
Summary:        System restore utility
License:        GPL-3.0-only
URL:            https://github.com/linuxmint/timeshift
#!RemoteAsset
Source:         %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dxapp=false

BuildRequires:  chrpath
BuildRequires:  fdupes
BuildRequires:  help2man
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(vte-2.91)

Requires:       rsync
Recommends:     btrfs-progs

%description
A system restore utility which takes snapshots of the system at regular
intervals. These snapshots can be restored at a later date to undo system
changes. Creates incremental snapshots using rsync or BTRFS snapshots
using BTRFS tools.

%prep -a
# rpmlint
sed -i -e 's|/usr/bin/env bash|/usr/bin/bash|g' src/timeshift-launcher

%install -a
# Cleanup rpath references
chrpath --delete %{buildroot}%{_bindir}/timeshift
chrpath --delete %{buildroot}%{_bindir}/timeshift-gtk
# Fix file permissions
chmod 0644 %{buildroot}%{_sysconfdir}/timeshift/default.json
chmod 0644 %{buildroot}%{_datadir}/metainfo/com.linuxmint.timeshift.metainfo.xml
chmod 0644 %{buildroot}%{_datadir}/timeshift/images/*.svg
# Remove as we use rpm/zypper
rm -f %{buildroot}%{_bindir}/timeshift-uninstall
# Remove appdata in preference to metadinfo
rm -rf %{buildroot}%{_datadir}/appdata
# Manually add log directories, set mode to 0750 and owned by root (boo#1165805)
install -d %{buildroot}%{_localstatedir}/log/timeshift
install -d %{buildroot}%{_localstatedir}/log/timeshift-btrfs

# TODO: fix the name error.
# Avoid illegal package names
rm -rf %{buildroot}%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages
%fdupes %{buildroot}%{_datadir}

%files -f %{name}.lang
%license LICENSES/*
%dir %{_sysconfdir}/timeshift
%config(noreplace) %{_sysconfdir}/timeshift/default.json
%{_bindir}/timeshift*
%{_datadir}/applications/timeshift-gtk.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/timeshift.1%{?ext_man}
%{_mandir}/man1/timeshift-gtk.1%{?ext_man}
%{_datadir}/metainfo/com.linuxmint.timeshift.metainfo.xml
%{_datadir}/polkit-1/actions/in.teejeetech.pkexec.timeshift.policy
%{_datadir}/pixmaps/timeshift.png
%{_datadir}/timeshift/
%attr(0750,root,root) %dir %{_localstatedir}/log/timeshift
%attr(0750,root,root) %dir %{_localstatedir}/log/timeshift-btrfs

%changelog
%autochangelog

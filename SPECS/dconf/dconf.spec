# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           dconf
Version:        0.49.0
Release:        %autorelease
Summary:        Configuration database system
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/dconf
#!RemoteAsset:  sha256:16a47e49a58156dbb96578e1708325299e4c19eea9be128d5bd12fd0963d6c36
Source:         https://download.gnome.org/sources/dconf/0.49/%{name}-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dgtk_doc=true

BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros
BuildRequires:  vala

Requires:       dbus
Requires:       glib >= 2.44.0

%description
dconf is a low-level configuration system. Its main purpose is to
provide a backend to GSettings on platforms that don't already
have configuration storage systems.

%package        devel
Summary:        Header files and libraries for %{name} development
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains header files, static library and other development files for dconf.

%install -a
mkdir -p %{buildroot}%{_sysconfdir}/dconf/profile

cat << EOF > %{buildroot}%{_sysconfdir}/dconf/profile/user
user-db:user
system-db:local
system-db:site
system-db:distro
EOF

mkdir -p %{buildroot}%{_sysconfdir}/dconf/db/local.d/locks
mkdir -p %{buildroot}%{_sysconfdir}/dconf/db/site.d/locks
mkdir -p %{buildroot}%{_sysconfdir}/dconf/db/distro.d/locks

%posttrans
%{_bindir}/dconf update

%post
%systemd_user_post dconf.service

%preun
%systemd_user_preun dconf.service

%postun
%systemd_user_postun_with_restart dconf.service

%files
%doc NEWS README HACKING
%license COPYING
%{_bindir}/dconf
%{_libexecdir}/dconf-service
%{_libdir}/libdconf.so.1*
%{_libdir}/gio/modules/libdconfsettings.so
%{_userunitdir}/dconf.service
%dir %{_sysconfdir}/dconf
%dir %{_sysconfdir}/dconf/db
%dir %{_sysconfdir}/dconf/db/local.d
%dir %{_sysconfdir}/dconf/db/local.d/locks
%dir %{_sysconfdir}/dconf/db/site.d
%dir %{_sysconfdir}/dconf/db/site.d/locks
%dir %{_sysconfdir}/dconf/db/distro.d
%dir %{_sysconfdir}/dconf/db/distro.d/locks
%dir %{_sysconfdir}/dconf/profile
%config(noreplace) %{_sysconfdir}/dconf/profile/user
%{_datadir}/dbus-1/services/ca.desrt.dconf.service
%{bash_completions_dir}/dconf
%{_mandir}/man?/*

%files devel
%{_includedir}/dconf
%{_libdir}/libdconf.so
%{_libdir}/pkgconfig/dconf.pc
%{_datadir}/vala
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/dconf

%changelog
%autochangelog

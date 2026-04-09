# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xdg-user-dirs
Version:        0.19
Release:        %autorelease
Summary:        Handles user special directories
License:        GPL-2.0-or-later AND MIT
URL:            https://freedesktop.org/wiki/Software/xdg-user-dirs
VCS:            git:https://gitlab.freedesktop.org/xdg/xdg-user-dirs
#!RemoteAsset:  sha256:e92deb929c10d4b29329397af8a2585101247f7e6177ac6f1d28e82130ed8c19
Source0:        https://user-dirs.freedesktop.org/releases/xdg-user-dirs-%{version}.tar.xz
BuildSystem:    autotools

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-xsl
BuildRequires:  libxslt

%description
Contains xdg-user-dirs-update that updates folders in a users
homedirectory based on the defaults configured by the administrator.

%conf -p
autoreconf -fiv -I ./m4

%install -a
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%post
%systemd_user_post xdg-user-dirs.service

%preun
%systemd_user_preun xdg-user-dirs.service

%postun
%systemd_user_postun_with_reload xdg-user-dirs.service

%files -f %{name}.lang
%license COPYING
%doc NEWS AUTHORS
%{_bindir}/xdg-user-dirs-update
%{_bindir}/xdg-user-dir
%config(noreplace) %{_sysconfdir}/xdg/user-dirs.conf
%config(noreplace) %{_sysconfdir}/xdg/user-dirs.defaults
%{_sysconfdir}/xdg/autostart/xdg-user-dirs.desktop
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_userunitdir}/xdg-user-dirs.service

%changelog
%autochangelog

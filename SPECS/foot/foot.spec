# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global foot_terminfo foot-extra
%global default_terminfo foot

Name:           foot
Version:        1.26.1
Release:        %autorelease
Summary:        Fast, lightweight and minimalistic Wayland terminal emulator
License:        MIT AND CC-BY-SA-4.0
URL:            https://codeberg.org/dnkl/foot
#!RemoteAsset:  sha256:4beb43f2d80719f53eb427f2185d43fe65bb82a763e25b3b1fe088d8947c2d73
Source0:        https://codeberg.org/dnkl/foot/releases/download/%{version}/foot-%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dterminfo-base-name=%{foot_terminfo}
BuildOption(conf):  -Ddefault-terminfo=%{default_terminfo}

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  python3
BuildRequires:  systemd-rpm-macros
BuildRequires:  libutempter-devel
BuildRequires:  pkgconfig(fcft)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(tllist)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(scdoc)

Requires:       hicolor-icon-theme

%description
Fast, lightweight and minimalistic Wayland terminal emulator.

%post
%systemd_user_post %{name}-server.{service,socket}

%preun
%systemd_user_preun %{name}-server.{service,socket}

%files
%license LICENSE
%config(noreplace) %{_sysconfdir}/xdg/foot/foot.ini
%{_bindir}/foot
%{_bindir}/footclient
%{_datadir}/foot/
%{_datadir}/applications/foot*.desktop
%{_datadir}/icons/hicolor/*/apps/foot.*
%{_datadir}/bash-completion/completions/foot*
%{_datadir}/fish/vendor_completions.d/foot*
%{_datadir}/zsh/site-functions/_foot*
%doc README.md CHANGELOG.md LICENSE
%{_mandir}/man1/foot*.1*
%{_mandir}/man5/foot.ini.5*
%{_mandir}/man7/foot-ctlseqs.7*
%{_userunitdir}/foot-server.service
%{_userunitdir}/foot-server.socket
%dir %{_datadir}/terminfo/f
%{_datadir}/terminfo/f/%{foot_terminfo}
%{_datadir}/terminfo/f/%{foot_terminfo}-direct

%changelog
%{?autochangelog}

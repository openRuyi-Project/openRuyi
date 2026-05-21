# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           wl-clipboard
Version:        2.3.0
Release:        %autorelease
Summary:        Command-line copy/paste utilities for Wayland
License:        GPL-3.0-or-later
URL:            https://github.com/bugaevc/wl-clipboard
#!RemoteAsset:  sha256:b4dc560973f0cd74e02f817ffa2fd44ba645a4f1ea94b7b9614dacc9f895f402
Source0:        https://github.com/bugaevc/wl-clipboard/archive/v%{version}/wl-clipboard-%{version}.tar.gz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-client)

%description
This project implements two command-line Wayland
clipboard utilities, wl-copy and wl-paste, that let
you easily copy data between the clipboard and Unix
pipes, sockets, files and so on.

%files
%doc README.md
%license COPYING
%{_bindir}/wl-copy
%{_bindir}/wl-paste
%{_mandir}/man1/wl-clipboard.1.*
%{_mandir}/man1/wl-copy.1.*
%{_mandir}/man1/wl-paste.1.*
%{_datadir}/bash-completion/completions/wl-*
%{_datadir}/fish/vendor_completions.d/wl-*
%{_datadir}/zsh/site-functions/_wl-*

%changelog
%autochangelog

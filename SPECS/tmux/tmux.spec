# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: ayostl <yao_xp@yeah.net>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           tmux
Version:        3.6a
Release:        %autorelease
Summary:        A terminal multiplexer
License:        ISC AND BSD-2-Clause AND BSD-3-Clause
URL:            https://tmux.github.io/
VCS:            git:https://github.com/tmux/tmux
#!RemoteAsset:  sha256:b6d8d9c76585db8ef5fa00d4931902fa4b8cbe8166f528f44fc403961a3f3759
Source0:        https://github.com/tmux/tmux/releases/download/%{version}/tmux-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --enable-sixel
BuildOption(conf):  --enable-systemd
BuildOption(conf):  --enable-utempter
BuildOption(conf):  --enable-utf8proc

BuildRequires:  pkgconfig(libevent) >= 2
BuildRequires:  (pkgconfig(tinfo) or pkgconfig(ncurses) or pkgconfig(ncursesw))
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  libutempter-devel
BuildRequires:  bison

%description
tmux is a "terminal multiplexer."  It enables a number of terminals (or
windows) to be accessed and controlled from a single terminal.  tmux is
intended to be a simple, modern, BSD-licensed alternative to programs such
as GNU Screen.

%files
%license COPYING
%{_mandir}/man1/tmux.1*
%{_bindir}/tmux

%changelog
%autochangelog

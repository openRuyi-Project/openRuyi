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
# SOURCE0 licensed under ISC AND BSD, SOURCE1 licensed under GPL-2.0-only
License:        ISC AND BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-only
URL:            https://tmux.github.io/
VCS:            git:https://github.com/tmux/tmux
#!RemoteAsset:  sha256:b6d8d9c76585db8ef5fa00d4931902fa4b8cbe8166f528f44fc403961a3f3759
Source0:        https://github.com/tmux/tmux/releases/download/%{version}/tmux-%{version}.tar.gz
#!RemoteAsset:  sha256:4e2179053376f4194b342249d75c243c1573c82c185bfbea008be1739048e709
Source1:        https://github.com/imomaliev/tmux-bash-completion/raw/refs/heads/master/completions/tmux
BuildSystem:    autotools

BuildOption(conf):  --enable-sixel
BuildOption(conf):  --enable-systemd
BuildOption(conf):  --enable-utempter
BuildOption(conf):  --enable-utf8proc

BuildRequires:  gcc
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

%install -a
install -Dpm 644 %{S:1} %{buildroot}%{_datadir}/bash-completion/completions/tmux

%files
%license COPYING
%{_mandir}/man1/tmux.1*
%{_bindir}/tmux
%{_datadir}/bash-completion/completions/tmux

%changelog
%autochangelog

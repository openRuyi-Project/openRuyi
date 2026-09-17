# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           tio
Version:        3.9
Release:        %autorelease
Summary:        Serial device I/O tool
License:        GPL-2.0-or-later
URL:            https://tio.github.io
VCS:            git:https://github.com/tio/tio.git
#!RemoteAsset:  sha256:06fe0c22e3e75274643c017928fbc85e86589bc1acd515d92f98eecd4bbab11b
Source0:        https://github.com/tio/tio/releases/download/v%{version}/tio-%{version}.tar.xz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(lua)

%description
tio is a command-line tool for communicating with serial TTY devices. It
supports automatic reconnection, logging, configuration profiles, Lua scripting,
and file transfers using the XMODEM and YMODEM protocols.

%files
%doc AUTHORS NEWS README.md
%license LICENSE
%{_bindir}/tio
%{_mandir}/man1/tio.1*
%{bash_completions_dir}/tio

%changelog
%autochangelog

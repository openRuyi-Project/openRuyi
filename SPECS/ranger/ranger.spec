# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ranger
Version:        1.9.4
Release:        %autorelease
Summary:        Vim-like console file manager
License:        GPL-3.0-only
URL:            https://ranger.github.io
#!RemoteAsset:  sha256:7ad75e0d1b29087335fbb1691b05a800f777f4ec9cba84faa19355075d7f0f89
Source0:        https://github.com/ranger/ranger/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{name} +auto

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
# ranger.gui.color calls curses.setupterm() at import time, so the import
# check needs a terminfo database and a known terminal.
BuildRequires:  ncurses

%description
ranger is a console file manager with VI key bindings. It provides a
minimalistic and nice curses interface with a view on the directory
hierarchy. It ships with rifle, a file launcher that is good at
automatically finding out which program to use for which file type.

%check -p
# ranger.gui.color runs curses.setupterm() on import; give it a known terminal.
export TERM=xterm

%files -f %{pyproject_files}
%license LICENSE
# ranger ships example/config plugin scripts under %%_docdir; their byte-compiled
# __pycache__ artifacts are not needed and would otherwise be unpackaged.
%exclude %{_datadir}/doc/ranger/config/__pycache__
%exclude %{_datadir}/doc/ranger/config/colorschemes/__pycache__
%exclude %{_datadir}/doc/ranger/examples/__pycache__
%exclude %{_datadir}/doc/ranger/tools/__pycache__

%changelog
%autochangelog

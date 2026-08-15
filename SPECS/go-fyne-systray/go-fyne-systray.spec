# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           systray
%define go_import_path  fyne.io/systray

Name:           go-fyne-systray
Version:        1.12.0
Release:        %autorelease
Summary:        Is a cross-platform Go library to place an icon and menu in the notification area
License:        Apache-2.0
URL:            https://github.com/fyne-io/systray
#!RemoteAsset:  sha256:4e73b29a0c15ba995beb63be2b6c398ed5aa8bf05297bd7e6bdf353128a87240
Source0:        https://github.com/fyne-io/systray/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/godbus/dbus/v5)

Provides:       go(fyne.io/systray) = %{version}

Requires:       go(github.com/godbus/dbus/v5)

%description
systray is a cross-platform Go library for placing an icon and menu in the notification area. This fork removes the GTK dependency and support for legacy Linux system trays.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog

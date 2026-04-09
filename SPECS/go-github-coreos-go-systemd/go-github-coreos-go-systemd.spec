# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-systemd
%define go_import_path  github.com/coreos/go-systemd
# systemd tests cannot done in a container environment - Julian
%define go_test_ignore_failure 1

Name:           go-github-coreos-go-systemd
Version:        22.7.0
Release:        %autorelease
Summary:        Go bindings to systemd socket activation, journal, D-Bus, and unit files
License:        Apache-2.0
URL:            https://github.com/coreos/go-systemd
#!RemoteAsset
Source0:        https://github.com/coreos/go-systemd/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/godbus/dbus)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/coreos/go-systemd) = %{version}

Requires:       go(github.com/godbus/dbus)
Requires:       go(golang.org/x/sys)

%description
Go bindings to systemd. The project has several packages:

 * activation - for writing and using socket activation from Go
 * daemon - for notifying systemd of service status changes
 * dbus - for starting/stopping/inspecting running services and units
 * journal - for writing to systemd's logging service, journald
 * sdjournal - for reading from journald by wrapping its C API
 * login1 - for integration with the systemd logind API
 * machine1 - for registering machines/containers with systemd
 * unit - for (de)serialization and comparison of unit files

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog

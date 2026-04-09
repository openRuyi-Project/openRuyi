# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           qmpbackup
Version:        0.52
Release:        %autorelease
Summary:        Backup utility for QEMU using QMP
License:        GPL-3.0-only
URL:            https://github.com/abbbi/qmpbackup
#!RemoteAsset
Source:         https://github.com/abbbi/qmpbackup/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l libqmpbackup

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-qemu-qmp
BuildRequires:  python3-colorlog

%description
qmpbackup is a tool to create backups of QEMU virtual machines using the
QEMU Monitor Protocol (QMP) features like drive-backup or blockdev-backup.
It supports bitmap based incremental backups.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/qmpbackup
%{_bindir}/qmprestore

%changelog
%autochangelog

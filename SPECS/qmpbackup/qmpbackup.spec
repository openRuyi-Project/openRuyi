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
#!RemoteAsset:  sha256:17374068cc83c0ac7d49fd5f6a5c671646bd34a237a8c9829246c876b3b1c60d
Source:         https://github.com/abbbi/qmpbackup/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l libqmpbackup

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(qemu-qmp)
BuildRequires:  python3dist(colorlog)

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

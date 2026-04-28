# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname rtslib-fb

Name:           python-%{srcname}
Version:        2.2.3
Release:        %autorelease
Summary:        API for Linux kernel LIO SCSI target
License:        Apache-2.0
URL:            https://github.com/open-iscsi/rtslib-fb
# This is a mess - 251
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/r/rtslib_fb/rtslib_fb-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l 'rtslib*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(systemd)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
API for generic Linux SCSI kernel target. Includes the 'target'
service and targetctl tool for restoring configuration.

%generate_buildrequires
%pyproject_buildrequires

%install -a
mkdir -p %{buildroot}%{_mandir}/man8/
mkdir -p %{buildroot}%{_mandir}/man5/
mkdir -p %{buildroot}%{_unitdir}
install -m 644 systemd/target.service %{buildroot}%{_unitdir}/target.service

%post
%systemd_post target.service

%preun
%systemd_preun target.service

%postun
%systemd_postun_with_restart target.service

%files -f %{pyproject_files}
%doc README.md
# Extra bin files
%{_bindir}/targetctl
%{_unitdir}/target.service

%changelog
%{?autochangelog}

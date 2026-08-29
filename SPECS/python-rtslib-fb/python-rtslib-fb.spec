# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname rtslib-fb
%global pypi_name rtslib_fb

Name:           python-%{srcname}
Version:        2.2.3
Release:        %autorelease
Summary:        API for Linux kernel LIO SCSI target
License:        Apache-2.0
URL:            https://github.com/open-iscsi/rtslib-fb
#!RemoteAsset:  sha256:c1053889b572fde4c0a9b468b508e4e838781364a60f4746e9c5f92aef459de6
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l 'rtslib*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(systemd)

Provides:       python3-%{srcname} = %{version}-%{release}
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
%autochangelog

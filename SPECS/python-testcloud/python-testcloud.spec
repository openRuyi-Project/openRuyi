# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname testcloud

Name:           python-%{srcname}
Version:        0.12.0
Release:        %autorelease
Summary:        Tool to download and boot cloud images locally
License:        GPL-2.0-or-later
URL:            https://github.com/teemtee/testcloud
#!RemoteAsset:  sha256:26fd97d24996dd487e2f3ce5a5d28ce884fb8899454392704ea48a25b73e170a
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(libvirt-python)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(peewee)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)

Requires:       xorriso

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Testcloud downloads and boots cloud images locally and provides both a command
line interface and a Python API.

%prep -a
# Use xorrisofs from the xorriso package to create the cloud-init seed image.
sed -i 's/"genisoimage"/"xorrisofs"/' testcloud/instance.py

%generate_buildrequires
%pyproject_buildrequires

%install -a
install -Dpm0644 manpages/testcloud.1 %{buildroot}%{_mandir}/man1/testcloud.1
install -Dpm0644 conf/99-testcloud-nonroot-libvirt-access.rules \
    %{buildroot}%{_udevrulesdir}/99-testcloud-nonroot-libvirt-access.rules
install -Dpm0644 conf/testcloud %{buildroot}%{_datadir}/bash-completion/completions/testcloud

%check -a
# Verify configuration loading and merging using upstream's in-memory database tests.
%pytest test/unit/test_config.py

%files -f %{pyproject_files}
%doc conf/settings-example.py
%doc README.md
%{_bindir}/testcloud
%{_bindir}/t7d
%{_datadir}/bash-completion/completions/%{srcname}
%{_mandir}/man1/testcloud.1*
%{_udevrulesdir}/99-testcloud-nonroot-libvirt-access.rules

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname h2

Name:           python-%{srcname}
Version:        4.3.0
Release:        %autorelease
Summary:        HTTP/2 State-Machine based protocol implementation
License:        MIT
URL:            https://github.com/python-hyper/hyper-h2
#!RemoteAsset:  sha256:6c59efe4323fa18b47a632221a1888bd7fde6249819beda254aeca909f221bf1
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
HTTP/2 Protocol Stack This repository contains a pure-Python
implementation of a HTTP/2 protocol stack. It's written from the ground up to
be embeddable in whatever program you choose to use, ensuring that you can
speak HTTP/2 regardless of your programming paradigm.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname Tempita

Name:           python-tempita
Version:        0.6.0
Release:        %autorelease
Summary:        A very small text templating language
License:        MIT
URL:            https://github.com/TurboGears/tempita
#!RemoteAsset:  sha256:76e15de0137e5011c22949cc15a5161f623fe6a31655751c6d765db6bbac27b6
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/tempita-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  tempita

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-tempita = %{version}-%{release}
%python_provide python3-tempita

%description
Tempita is a small templating language for text substitution.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

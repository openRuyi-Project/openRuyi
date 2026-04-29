# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname smdebug-rulesconfig
%global pypi_name smdebug_rulesconfig

Name:           python-%{srcname}
Version:        1.0.1
Release:        %autorelease
Summary:        Amazon SageMaker Debugger RulesConfig
License:        Apache-2.0
URL:            https://github.com/awslabs/sagemaker-debugger-rulesconfig
#!RemoteAsset:  sha256:7a19e6eb2e6bcfefbc07e4a86ef7a88f32495001a038bf28c7d8e77ab793fcd6
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{pypi_name}-%{version}.tar.gz
#!RemoteAsset:  sha256:09e8a9bcec8067104652c168685ab0931e7868f9c8284b66f5ae6edae5f1130b
Source1:        https://raw.githubusercontent.com/awslabs/sagemaker-debugger-rulesconfig/%{version}/LICENSE
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Amazon SageMaker Debugger is designed to be a debugger for
machine learning models. It lets you go beyond just looking at
scalars like losses and accuracies during training and gives you full
visibility into all tensors 'flowing through the graph' during training or inference.

%prep -a
cp %{SOURCE1} .

%generate_buildrequires
%pyproject_buildrequires

%install -a
# Remove the tests directory that is incorrectly installed.
rm -rf %{buildroot}%{python3_sitelib}/tests/

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog

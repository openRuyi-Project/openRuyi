# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname gradio

Name:           python-%{srcname}
Version:        6.16.0
Release:        %autorelease
Summary:        Python library for easily interacting with trained machine learning models
License:        Apache-2.0
URL:            https://github.com/gradio-app/gradio
#!RemoteAsset:  sha256:a48d03ffb436644265e4386388ad8a50ec183c8e1fdd3bae0548f7f229c474da
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# Triggers FileNotFoundError by scanning a local 'themes' directory during module import.
BuildOption(check):  -e gradio.themes.app
# Triggers network error by downloading a remote AWS S3 image during module import.
BuildOption(check):  -e gradio.themes.builder_app

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Build and share delightful machine learning apps, all in Python.

%prep -a
sed -i 's/tomlkit>=0.12.0,<0.15.0/tomlkit>=0.12.0/g' requirements.txt
sed -i 's/Requires-Dist: tomlkit<0.15.0,>=0.12.0/Requires-Dist: tomlkit>=0.12.0/g' PKG-INFO
# Gradio and gradio-client are released together; accept the newer compatible
# client already carried by openRuyi instead of requiring the exact PyPI lock.
sed -i 's/gradio_client==2.5.0/gradio_client>=2.5.0/' requirements.txt
sed -i 's/Requires-Dist: gradio-client==2.5.0/Requires-Dist: gradio-client>=2.5.0/' PKG-INFO

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/gradio
%{_bindir}/upload_theme
%{python3_sitelib}/gradio/components/api_component.pyi
%{python3_sitelib}/gradio/components/custom_html_components/audio_gallery.pyi
%{python3_sitelib}/gradio/components/custom_html_components/colored_checkbox_group.pyi
%{python3_sitelib}/gradio/hash_seed.txt

%changelog
%autochangelog

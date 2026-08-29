# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global flavor @BUILD_FLAVOR@%{nil}
%global srcname setuptools
%global python_wheel_name %{srcname}-%{version}-py3-none-any.whl

# Virtual provides for the packages bundled by setuptools.
# Bundled packages are defined in multiple files. Generate the list with:
# pip freeze --path setuptools/_vendor > vendored.txt
# %%{_rpmconfigdir}/pythonbundles.py --namespace 'python%3dist' vendored.txt
%global bundled %{expand:
Provides: bundled(python3dist(autocommand)) = 2.2.2
Provides: bundled(python3dist(backports-tarfile)) = 1.2
Provides: bundled(python3dist(importlib-metadata)) = 8.7.1
Provides: bundled(python3dist(jaraco-context)) = 6.1
Provides: bundled(python3dist(jaraco-functools)) = 4.4
Provides: bundled(python3dist(jaraco-text)) = 4
Provides: bundled(python3dist(more-itertools)) = 10.8
Provides: bundled(python3dist(packaging)) = 26
Provides: bundled(python3dist(platformdirs)) = 4.4
Provides: bundled(python3dist(tomli)) = 2.4
Provides: bundled(python3dist(wheel)) = 0.46.3
Provides: bundled(python3dist(zipp)) = 3.23
}

# If it is set to 1, the bootstrap process will be included
%if "%{flavor}" == "bootstrap"
%bcond bootstrap 1
%else
%bcond bootstrap 0
%endif

%if %{with bootstrap}
Name:           python-%{srcname}-bootstrap
%else
Name:           python-%{srcname}
%endif
Version:        82.0.1
Release:        %autorelease
Summary:        Easily build and distribute Python packages
License:        MIT AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0) AND Python-2.0.1 AND LGPL-3.0-only
URL:            https://pypi.python.org/pypi/setuptools
# TODO: Use %%{pypi_source %%{srcname} %%{version}} in the future - 251
#       Otherwise https://files.pythonhosted.org/packages/source/a/abc/%%{srcname}-%%{version}.tar.gz
#!RemoteAsset:  sha256:7d872682c5d01cfde07da7bccc7b65469d3dca203318515ada1de5eda35efbf9
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python3)

%if %{with bootstrap}
BuildRequires:  unzip
%endif

# python3 bootstrap: this is built before the final build of python3, which
# adds the dependency on python3-rpm-generators, so we require it manually
BuildRequires:  python3-rpm-generators
# we also use %%{_pyproject_wheeldir}, so an explicit requirement on the pyproject-macros is needed
BuildRequires:  pyproject-rpm-macros

%if %{without bootstrap}
# Not to use the pre-generated egg-info, we use setuptools from previous build to generate it
BuildRequires:  python-setuptools
%endif

%{bundled}

# It can't self provide this...
Provides:       python3-setuptools = %{version}-%{release}

%description
Setuptools is a collection of enhancements to the Python distutils that allow
you to more easily build and distribute Python packages, especially ones that
have dependencies on other packages.

%package     -n %{python_wheel_pkg_prefix}-%{srcname}-wheel
Summary:        The setuptools wheel
%{bundled}

%description -n %{python_wheel_pkg_prefix}-%{srcname}-wheel
A Python wheel of setuptools to use with venv.

%prep
%autosetup -p1 -n %{srcname}-%{version}

# Strip shbang
find setuptools -name \*.py | xargs sed -i -e '1 {/^#!\//d}'
# Remove bundled exes
rm -f setuptools/*.exe
# Don't ship these
rm -r docs/conf.py

%if %{without bootstrap}
%generate_buildrequires
%pyproject_buildrequires -r
%endif

%build
%if %{with bootstrap}
%{python3} setup.py bdist_wheel
mkdir -p %{_pyproject_wheeldir}
mv dist/%{python_wheel_name} %{_pyproject_wheeldir}
%else
%pyproject_wheel
%endif

%install
%if %{with bootstrap}
mkdir -p %{buildroot}%{python3_sitelib}
unzip %{_pyproject_wheeldir}/%{python_wheel_name} -d %{buildroot}%{python3_sitelib} -x setuptools-%{version}.dist-info/RECORD
echo rpm > %{buildroot}%{python3_sitelib}/setuptools-%{version}.dist-info/INSTALLER
%else
%pyproject_install
%pyproject_save_files -l setuptools _distutils_hack
sed -Ei '/\/tests\b/d' %{pyproject_files}
%endif

# https://github.com/pypa/setuptools/issues/2709
find %{buildroot}%{python3_sitelib} -name tests -print0 | xargs -0 rm -r

# Install the wheel for the python-setuptools-wheel package
mkdir -p %{buildroot}%{python_wheel_dir}
install -p %{_pyproject_wheeldir}/%{python_wheel_name} -t %{buildroot}%{python_wheel_dir}

%files %{?!with_bootstrap:-f %{pyproject_files}}
%doc docs/* NEWS.rst README.rst
%{python3_sitelib}/distutils-precedence.pth
%if %{with bootstrap}
%{python3_sitelib}/setuptools-%{version}.dist-info/
%license %{python3_sitelib}/setuptools-%{version}.dist-info/licenses/LICENSE
%{python3_sitelib}/setuptools/
%{python3_sitelib}/_distutils_hack/
%endif

%files -n %{python_wheel_pkg_prefix}-%{srcname}-wheel
%license LICENSE
# we own the dir for simplicity
%dir %{python_wheel_dir}/
%{python_wheel_dir}/%{python_wheel_name}

%changelog
%autochangelog

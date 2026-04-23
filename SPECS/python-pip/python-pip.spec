# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pip
%global python_wheel_name %{srcname}-%{version}-py3-none-any.whl

# Set this to 0 if we have proper bash
%bcond bash 1

# Virtual provides for the packages bundled by pip.
# You can generate it with:
# %%{_rpmconfigdir}/pythonbundles.py --namespace 'python%%{1}dist' src/pip/_vendor/vendor.txt
%global bundled() %{expand:
Provides:       bundled(python%{1}dist(cachecontrol)) = 0.14.3
Provides:       bundled(python%{1}dist(certifi)) = 2025.10.5
Provides:       bundled(python%{1}dist(dependency-groups)) = 1.3.1
Provides:       bundled(python%{1}dist(distlib)) = 0.4
Provides:       bundled(python%{1}dist(distro)) = 1.9
Provides:       bundled(python%{1}dist(idna)) = 3.10
Provides:       bundled(python%{1}dist(msgpack)) = 1.1.2
Provides:       bundled(python%{1}dist(packaging)) = 25
Provides:       bundled(python%{1}dist(platformdirs)) = 4.5
Provides:       bundled(python%{1}dist(pygments)) = 2.19.2
Provides:       bundled(python%{1}dist(pyproject-hooks)) = 1.2
Provides:       bundled(python%{1}dist(requests)) = 2.32.5
Provides:       bundled(python%{1}dist(resolvelib)) = 1.2.1
Provides:       bundled(python%{1}dist(rich)) = 14.2
Provides:       bundled(python%{1}dist(setuptools)) = 70.3
Provides:       bundled(python%{1}dist(tomli)) = 2.3
Provides:       bundled(python%{1}dist(tomli-w)) = 1.2
Provides:       bundled(python%{1}dist(truststore)) = 0.10.4
Provides:       bundled(python%{1}dist(urllib3)) = 1.26.20
}

Name:           python-%{srcname}
Version:        25.3
Release:        %autorelease
Summary:        A tool for installing and managing Python packages
License:        MIT AND Python-2.0.1 AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MPL-2.0 AND (Apache-2.0 OR BSD-2-Clause)
URL:            https://pip.pypa.io/
#!RemoteAsset:  sha256:6f4d5c31324f7f998ec7c626c3a1543b5db5fb82c941c2b2952eeee183340d8f
Source0:        https://github.com/pypa/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%undefine _py3_shebang_s

BuildRequires:  pkgconfig(python3)
# python3 bootstrap: this is rebuilt before the final build of python3, which
# adds the dependency on python3-rpm-generators, so we require it manually
# Note that the package prefix is always python3-, even if we build for 3.X
BuildRequires:  python3-rpm-generators
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(flit-core)
%if %{without bash}
BuildRequires:  bash-completion
%endif
BuildRequires:  ca-certificates

Provides:       pip = %{version}-%{release}
Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

Requires:       ca-certificates
# Virtual provides for the packages bundled by pip:
%{bundled 3}

%description
pip is a package management system used to install and manage software packages
written in Python. Many packages can be found in the Python Package Index
(PyPI). pip is a recursive acronym that can stand for either "Pip Installs
Packages" or "Pip Installs Python".

%package     -n %{python_wheel_pkg_prefix}-%{srcname}-wheel
Summary:        The pip wheel
Requires:       ca-certificates
# Virtual provides for the packages bundled by pip:
%{bundled 3}

%description -n %{python_wheel_pkg_prefix}-%{srcname}-wheel
A Python wheel of pip to use with venv.

# We use our own way to build python packages
%prep
%autosetup -p1 -n %{srcname}-%{version}

# Remove windows executable binaries
rm -v src/pip/_vendor/distlib/*.exe
sed -i '/\.exe/d' pyproject.toml

%build
export PYTHONPATH=./src/
%pyproject_wheel

%install
export PYTHONPATH=./src/
%pyproject_install
%pyproject_save_files -l pip

# Provide symlinks to executables
mv %{buildroot}%{_bindir}/pip %{buildroot}%{_bindir}/pip%{python3_version}
rm %{buildroot}%{_bindir}/pip3

%global alternate_names pip-%{python3_version} pip-3 pip3 pip
for pip in %{alternate_names}; do
    ln -s ./pip%{python3_version} %{buildroot}%{_bindir}/$pip
done

%if %{without bash}
mkdir -p %{buildroot}%{bash_completions_dir}
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    %{buildroot}%{_bindir}/pip%{python3_version} completion --bash \
    > %{buildroot}%{bash_completions_dir}/pip%{python3_version}

# Make bash completion apply to all alternate names symlinks we install
sed -i -e "s/^\\(complete.*\\) pip%{python3_version}\$/\\1 pip%{python3_version} %{alternate_names}/" \
    -e s/_pip_completion/_pip%{python3_version_nodots}_completion/ \
    %{buildroot}%{bash_completions_dir}/pip%{python3_version}
%endif

mkdir -p %{buildroot}%{python_wheel_dir}
install -p %{_pyproject_wheeldir}/%{python_wheel_name} -t %{buildroot}%{python_wheel_dir}

%files -f %{pyproject_files}
%doc README.rst
%{_bindir}/pip
%{_bindir}/pip3
%{_bindir}/pip-3
%{_bindir}/pip%{python3_version}
%{_bindir}/pip-%{python3_version}
%if %{without bash}
%dir %{bash_completions_dir}
%{bash_completions_dir}/pip%{python3_version}
%endif

%files -n %{python_wheel_pkg_prefix}-%{srcname}-wheel
%license LICENSE.txt
# we own the dir for simplicity
%dir %{python_wheel_dir}/
%{python_wheel_dir}/%{python_wheel_name}

%changelog
%autochangelog

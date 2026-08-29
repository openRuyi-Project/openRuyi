# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# To enable these, change to 1
%bcond manpages 0

%global srcname rpmautospec
%global fish_completions_dir %{_datadir}/fish/vendor_completions.d
%global zsh_completions_dir %{_datadir}/zsh/site-functions

Name:           python-%{srcname}
Version:        0.8.3
Release:        %autorelease
Summary:        Package and CLI tool to generate release fields and changelogs
License:        MIT AND GPL-2.0-only WITH GCC-exception-2.0 AND (MIT OR GPL-2.0-or-later WITH GCC-exception-2.0)
URL:            https://github.com/fedora-infra/rpmautospec
#!RemoteAsset:  sha256:66fa5540871c1140ed051c89b0624f14eaf59609452448360fa58cd7211e7a41
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
Source1:        rpmautospec.in
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
%if %{with manpages}
BuildRequires:  python3dist(click-man)
%endif
BuildRequires:  rpm-build
BuildRequires:  libgit2
BuildRequires:  bash-completion

Requires:       rpm-build
Requires:       python-click

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A package and CLI tool to generate RPM release fields and changelogs.

%package     -n %{srcname}
Summary:        CLI tool for generating RPM releases and changelogs
Provides:       bundled(python3dist(rpmautospec)) = %{version}
Provides:       bundled(python3dist(rpmautospec-core)) = %((rpm -q python3-rpmautospec-core --qf '%%{version}\n' || echo 0) | tail -n1)
Requires:       libgit2

%description -n %{srcname}
CLI tool for generating RPM releases and changelogs

%package     -n %{srcname}-rpm-macros
Summary:        Rpmautospec RPM macros for local rpmbuild
Requires:       rpm

%description -n %{srcname}-rpm-macros
This package contains RPM macros with placeholders for building rpmautospec
enabled packages locally.

%generate_buildrequires
%pyproject_buildrequires -x all

%install -a
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m 644 rpm_macros.d/macros.rpmautospec %{buildroot}%{_rpmmacrodir}/

# Shell completion
for shell_path in \
        bash:%{bash_completions_dir}/rpmautospec \
        fish:%{fish_completions_dir}/rpmautospec.fish \
        zsh:%{zsh_completions_dir}/_rpmautospec; do
    shell="${shell_path%%:*}"
    path="${shell_path#*:}"
    dir="${path%/*}"

    install -m 755 -d "%{buildroot}${dir}"

    PYTHONPATH=%{buildroot}%{python3_sitelib} \
    _RPMAUTOSPEC_COMPLETE="${shell}_source" \
    %{__python3} -c \
    "import sys; sys.argv[0] = 'rpmautospec'; from rpmautospec.cli import cli; sys.exit(cli())" \
    > "%{buildroot}${path}"
done

# Fill in the real version for the fallback method
touch -r %{buildroot}%{python3_sitelib}/rpmautospec/version.py timestamp
sed -i -e 's|0\.0\.0|%{version}|g' %{buildroot}%{python3_sitelib}/rpmautospec/version.py
touch -r timestamp %{buildroot}%{python3_sitelib}/rpmautospec/version.py

# Install bootstrapping copies of rpmautospec, rpmautospec_core packages
mkdir -p %{buildroot}%{_datadir}/rpmautospec-fallback
cp -r %{python3_sitelib}/rpmautospec_core %{buildroot}%{_datadir}/rpmautospec-fallback/
cp -r %{buildroot}%{python3_sitelib}/rpmautospec %{buildroot}%{_datadir}/rpmautospec-fallback/
find %{buildroot}%{_datadir}/rpmautospec-fallback \
    -depth -type d -a -name __pycache__ -exec rm -r {} \;

# Override the standard executable with a custom one that knows how to fall back
sed -e 's|@PYTHON3@|%{python3} -%{py3_shebang_flags}|g; s|@DATADIR@|%{_datadir}|g' \
    < %{S:1} \
    > %{buildroot}%{_bindir}/rpmautospec
chmod 755 %{buildroot}%{_bindir}/rpmautospec
touch -r %{S:1} %{buildroot}%{_bindir}/rpmautospec

%files -f %{pyproject_files}
%doc README.rst

%files -n %{srcname}
%{_bindir}/rpmautospec
%{_datadir}/rpmautospec-fallback
%if %{with manpages}
%{_mandir}/man1/rpmautospec*.1*
%endif
%dir %{bash_completions_dir}
%{bash_completions_dir}/rpmautospec
%dir %{fish_completions_dir}
%{fish_completions_dir}/rpmautospec.fish
%dir %{zsh_completions_dir}
%{zsh_completions_dir}/_rpmautospec

%files -n rpmautospec-rpm-macros
%{_rpmmacrodir}/macros.rpmautospec

%changelog
%autochangelog

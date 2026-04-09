# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Originally extracted from Fedora Project
# Authors: The Fedora Project Contributors

%define mockversion 6.4

Name:           mock-core-configs
Version:        43.2
Release:        %autorelease
Summary:        Mock core config files basic chroots
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/mock
# What the hell... Please check the release page!!! - 251
#!RemoteAsset
Source0:        %{url}/releases/download/mock-%{mockversion}-1/%{name}-%{version}.tar.gz
BuildArch:      noarch

Provides:       mock-configs

Recommends:     dnf-utils
Recommends:     dnf5
Recommends:     dnf5-plugins

Requires:       mock
Requires:       mock-filesystem

%description
Mock configuration files which allow you to create chroots for Alma Linux,
Amazon Linux, CentOS, CentOS Stream, Circle Linux, EuroLinux, Fedora, Fedora EPEL, Mageia,
Navy Linux, OpenMandriva Lx, openSUSE, Oracle Linux, Red Hat Enterprise Linux,
Rocky Linux and various other specific or combined chroots.

%prep
%setup -q

%build
# No Build

%install
mkdir -p %{buildroot}%{_sysconfdir}/mock/eol/templates
mkdir -p %{buildroot}%{_sysconfdir}/mock/templates
cp -a etc/mock/*.cfg %{buildroot}%{_sysconfdir}/mock
cp -a etc/mock/templates/*.tpl %{buildroot}%{_sysconfdir}/mock/templates
cp -a etc/mock/eol/*cfg %{buildroot}%{_sysconfdir}/mock/eol
cp -a etc/mock/eol/templates/*.tpl %{buildroot}%{_sysconfdir}/mock/eol/templates

# generate files section with config - there is many of them
find %{buildroot}%{_sysconfdir}/mock -name "*.cfg" -o -name '*.tpl' \
    | grep -v chroot-aliases \
    | sed -e "s|^%{buildroot}|%%config(noreplace) |" >> %{name}.cfgs
echo "%%config %{_sysconfdir}/mock/chroot-aliases.cfg" >> %{name}.cfgs

# just for %%ghosting purposes
ln -s fedora-rawhide-x86_64.cfg %{buildroot}%{_sysconfdir}/mock/default.cfg
# bash-completion
if [ -d %{buildroot}%{_datadir}/bash-completion ]; then
    echo %{_datadir}/bash-completion/completions/mock >> %{name}.cfgs
    echo %{_datadir}/bash-completion/completions/mockchain >> %{name}.cfgs
elif [ -d %{buildroot}%{_sysconfdir}/bash_completion.d ]; then
    echo %{_sysconfdir}/bash_completion.d/mock >> %{name}.cfgs
fi

# reference valid mock.rpm's docdir with example site-defaults.cfg
mock_docs=%{_pkgdocdir}
mock_docs=${mock_docs//mock-core-configs/mock}
mock_docs=${mock_docs//-%version/-*}
sed -i "s~@MOCK_DOCS@~$mock_docs~" %{buildroot}%{_sysconfdir}/mock/site-defaults.cfg

%post
mock_arch=$(uname -m)
distro_id=$(. /etc/os-release; echo $ID)
cfg=$distro_id-$mock_arch.cfg
if [ -e %{_sysconfdir}/mock/$cfg ]; then
    if [ "$(readlink %{_sysconfdir}/mock/default.cfg)" != "$cfg" ]; then
        ln -s $cfg %{_sysconfdir}/mock/default.cfg 2>/dev/null || ln -s -f $cfg %{_sysconfdir}/mock/default.cfg.rpmnew
    fi
else
    echo "Warning: file %{_sysconfdir}/mock/$cfg does not exist."
    echo "         unable to update %{_sysconfdir}/mock/default.cfg"
fi
:

%files -f %{name}.cfgs
%license COPYING
%doc README
%ghost %config(noreplace,missingok) %{_sysconfdir}/mock/default.cfg

%changelog
%autochangelog

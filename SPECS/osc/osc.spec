# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           osc
Version:        1.21.0
Release:        %autorelease
Summary:        The Command Line Interface to work with an Open Build Service
License:        GPL-2.0-or-later
URL:            https://github.com/openSUSE/osc
#!RemoteAsset:  sha256:6579381095a8a6675a6ffca4c894a2e5706fe19c45f2e9a18631d75e00bed051
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3dist(argparse-manpage)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3-devel
BuildRequires:  python3dist(distro)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(progressbar2)
BuildRequires:  python3-rpm
BuildRequires:  python3dist(ruamel-yaml)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(urllib3)
BuildRequires:  git-core
BuildRequires:  bash-completion

Requires:       python3dist(cryptography)
Requires:       python3-rpm
Requires:       python3dist(urllib3)
Requires:       python3dist(lxml)

%description
Commandline client for the Open Build Service.

See http://en.opensuse.org/openSUSE:OSC , as well as
http://en.opensuse.org/openSUSE:Build_Service_Tutorial for a general
introduction.

%prep
%autosetup -p1

%build
%pyproject_wheel

# write rpm macros
cat << EOF > macros.osc
%%osc_plugin_dir %{_prefix}/lib/osc-plugins
EOF

# build man page
PYTHONPATH=. argparse-manpage \
    --output=osc.1 \
    --format=single-commands-section \
    --module=osc.commandline \
    --function=argparse_manpage_get_parser \
    --project-name=osc \
    --prog=osc \
    --description="Command-line client for Open Build Service" \
    --author="Contributors to the osc project. See the project's GIT history for the complete list." \
    --url="https://github.com/openSUSE/osc/"

PYTHONPATH=. argparse-manpage \
    --output=git-obs.1 \
    --format=single-commands-section \
    --module=osc.commandline_git \
    --function=argparse_manpage_get_parser \
    --project-name=osc \
    --prog=git-obs \
    --description="Git based command-line client for Open Build Service" \
    --author="Contributors to the osc project. See the project's GIT history for the complete list." \
    --url="https://github.com/openSUSE/osc/"

%install
%pyproject_install

# install completions
mkdir -p %{buildroot}%{_localstatedir}/lib/osc-plugins
install -Dm0644 contrib/complete.csh %{buildroot}%{_sysconfdir}/profile.d/osc.csh
install -Dm0644 contrib/git-obs-complete.zsh %{buildroot}%{_datadir}/zsh/functions/Completion/git-obs.zsh
install -Dm0644 contrib/complete.sh %{buildroot}%{bash_completions_dir}/osc
install -Dm0644 contrib/git-obs-complete.bash %{buildroot}%{bash_completions_dir}/git-obs.bash
install -Dm0755 contrib/osc.complete %{buildroot}%{_datadir}/osc/complete
install -Dm0644 contrib/osc.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/osc.fish
install -Dm0644 contrib/git-obs-complete.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/git-obs.fish

# symlink /usr/bin/git-obs to /usr/libexec/git/obs
mkdir -p %{buildroot}%{_libexecdir}/git
ln -s %{_bindir}/git-obs %{buildroot}%{_libexecdir}/git/obs

# install rpm macros
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d/
install -Dm0644 macros.osc %{buildroot}%{_rpmmacrodir}/macros.osc

# install man page
install -Dm0644 osc.1 %{buildroot}%{_mandir}/man1/osc.1
install -Dm0644 git-obs.1 %{buildroot}%{_mandir}/man1/git-obs.1

# inject argcomplete marker to the generated git-obs executable
sed -i '3i # PYTHON_ARGCOMPLETE_OK'  %{buildroot}%{_bindir}/git-obs

%files
%doc AUTHORS README.md NEWS
%license COPYING
%{_bindir}/osc*
%{_bindir}/git-obs
%{_bindir}/git-osc-precommit-hook
%{_libexecdir}/git/obs
%{python3_sitelib}/osc*
%{_sysconfdir}/profile.d/osc.csh
%{_datadir}/zsh/functions/Completion/git-obs.zsh
%{bash_completions_dir}/osc
%{bash_completions_dir}/git-obs.bash
%{_datadir}/fish/vendor_completions.d/osc.fish
%{_datadir}/fish/vendor_completions.d/git-obs.fish
%dir %{_localstatedir}/lib/osc-plugins
%{_mandir}/man1/osc.*
%{_mandir}/man1/git-obs.*
%{_datadir}/osc
%{_rpmconfigdir}/macros.d/macros.osc

%changelog
%autochangelog

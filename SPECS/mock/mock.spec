# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Originally extracted from Fedora Project
# Authors: The Fedora Project Contributors

# Enable set to 1
%bcond lint 0

Name:           mock
Version:        6.5
Release:        %autorelease
Summary:        Builds packages inside chroots
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/mock
#!RemoteAsset:  sha256:c3672842b68f0e58f331ec6280be516a830afbbb607edfdd5dee09847fbde687
Source0:        %{url}/releases/download/%{name}-%{version}-1/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  bash-completion
BuildRequires:  perl
BuildRequires:  python3dist(backoff)
BuildRequires:  python3-devel
BuildRequires:  python3-rpm
BuildRequires:  python3-rpmautospec-core
BuildRequires:  python3dist(argparse-manpage)
BuildRequires:  python3dist(requests)
%if %{with lint}
BuildRequires:  python3dist(pylint)
%endif

Recommends:     dnf-utils
Recommends:     dnf5
Recommends:     dnf5-plugins

Requires:       python3dist(distro)
Requires:       python3dist(jinja2)
Requires:       python3dist(requests)
Requires:       python3-rpm
Requires:       python3dist(pyroute2)
Requires:       python3dist(templated-dictionary)
Requires:       python3dist(backoff)
Requires:       mock-configs
Requires:       %{name}-filesystem = %{version}-%{release}
Requires:       tar
Requires:       createrepo_c
Requires:       systemd
Requires:       coreutils
Requires:       util-linux
Requires:       procps-ng
Requires:       shadow
Recommends:     btrfs-progs

%description
Mock takes an SRPM and builds it in a chroot.

%package        scm
Summary:        Mock SCM integration module
Requires:       %{name} = %{version}-%{release}
Recommends:     cvs
Recommends:     git
Recommends:     subversion
Recommends:     tar

%description    scm
Mock SCM integration module.

%package        lvm
Summary:        LVM plugin for mock
Requires:       %{name} = %{version}-%{release}
Requires:       lvm2

%description    lvm
Mock plugin that enables using LVM as a backend and support creating snapshots
of the buildroot.

%package        rpmautospec
Summary:        Rpmautospec plugin for mock
Requires:       %{name} = %{version}-%{release}
Requires:       python3-rpmautospec-core

%description    rpmautospec
Mock plugin that preprocesses spec files using rpmautospec.

%package        filesystem
Summary:        Mock filesystem layout
Requires(pre):  shadow
BuildRequires:  systemd-rpm-macros

%description    filesystem
Filesystem layout and group for Mock.

%prep
%setup -q
for file in py/mock.py py/mock-parse-buildlog.py; do
  sed -i 1"s|#!/usr/bin/python3 |#!%{__python} |" $file
done

%build
for i in py/mockbuild/constants.py py/mock-parse-buildlog.py; do
    sed -i \
        -e 's|^VERSION[[:space:]]*=.*|VERSION="%{version}"|' \
        -e 's|^SYSCONFDIR[[:space:]]*=.*|SYSCONFDIR="%{_sysconfdir}"|' \
        -e 's|^PYTHONDIR[[:space:]]*=.*|PYTHONDIR="%{python_sitelib}"|' \
        -e 's|^PKGPYTHONDIR[[:space:]]*=.*|PKGPYTHONDIR="%{python_sitelib}/mockbuild"|' \
        "$i"
done
for i in docs/mock.1 docs/mock-parse-buildlog.1; do
    sed -i 's|@VERSION@|%{version}"|' "$i"
done

argparse-manpage --pyfile ./py/mock-hermetic-repo.py --function _argparser > mock-hermetic-repo.1

%install
mkdir -p %{buildroot}%{_sysconfdir}/mock/eol/templates
mkdir -p %{buildroot}%{_sysconfdir}/mock/templates

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_libexecdir}/mock
install mockchain %{buildroot}%{_bindir}/mockchain
install py/mock-hermetic-repo.py %{buildroot}%{_bindir}/mock-hermetic-repo
install py/mock-parse-buildlog.py %{buildroot}%{_bindir}/mock-parse-buildlog
install py/mock.py %{buildroot}%{_libexecdir}/mock/mock
ln -s consolehelper %{buildroot}%{_bindir}/mock

install -d %{buildroot}%{_sysconfdir}/pam.d
cp -a etc/pam/* %{buildroot}%{_sysconfdir}/pam.d/

install -d %{buildroot}%{_sysconfdir}/mock
cp -a etc/mock/* %{buildroot}%{_sysconfdir}/mock/

install -d %{buildroot}%{_sysconfdir}/security/console.apps/
cp -a etc/consolehelper/mock %{buildroot}%{_sysconfdir}/security/console.apps/%{name}

install -d %{buildroot}%{_datadir}/bash-completion/completions/
cp -a etc/bash_completion.d/* %{buildroot}%{_datadir}/bash-completion/completions/
ln -s mock %{buildroot}%{_datadir}/bash-completion/completions/mock-parse-buildlog

install -d %{buildroot}%{_sysconfdir}/pki/mock
cp -a etc/pki/* %{buildroot}%{_sysconfdir}/pki/mock/

install -d %{buildroot}%{python_sitelib}/
cp -a py/mockbuild %{buildroot}%{python_sitelib}/

install -d %{buildroot}%{_mandir}/man1
cp -a docs/mock.1 docs/mock-parse-buildlog.1 mock-hermetic-repo.1 %{buildroot}%{_mandir}/man1/
install -d %{buildroot}%{_datadir}/cheat
cp -a docs/mock.cheat %{buildroot}%{_datadir}/cheat/mock

install -d %{buildroot}/var/lib/mock
install -d %{buildroot}/var/cache/mock

mkdir -p %{buildroot}%{_docdir}/%{name}
install -p -m 0644 docs/buildroot-lock-schema-*.json %{buildroot}%{_docdir}/%{name}
install -p -m 0644 docs/site-defaults.cfg %{buildroot}%{_docdir}/%{name}

mkdir -p %{buildroot}%{_sysusersdir}
install -p -D -m 0644 %{name}.conf %{buildroot}%{_sysusersdir}

sed -i 's/^_MOCK_NVR = None$/_MOCK_NVR = "%name-%version-%release"/' \
    %{buildroot}%{_libexecdir}/mock/mock

%pre filesystem
# Some of these older distributions do not ship with the %%sysusers_*_compat.
# Instead of another ifdef/else here, we prefer to hardcode the scriptlet
# content here.
getent group 'mock' >/dev/null || groupadd -f -g '135' -r 'mock' || :

%files
%dir %{_docdir}/%{name}/
%doc %{_docdir}/%{name}/site-defaults.cfg
%doc %{_docdir}/%{name}/buildroot-lock-schema-*.json
%{_datadir}/bash-completion/completions/mock
%{_datadir}/bash-completion/completions/mock-parse-buildlog
%{_bindir}/mock
%{_bindir}/mockchain
%{_bindir}/mock-hermetic-repo
%{_bindir}/mock-parse-buildlog
%{_libexecdir}/mock
%{python_sitelib}/*
%exclude %{python_sitelib}/mockbuild/scm.*
%exclude %{python_sitelib}/mockbuild/plugins/lvm_root.*
%exclude %{python_sitelib}/mockbuild/plugins/rpmautospec.*
%config(noreplace) %{_sysconfdir}/%{name}/*.ini
%config(noreplace) %{_sysconfdir}/%{name}/hermetic-build.cfg
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%config(noreplace) %{_sysconfdir}/security/console.apps/%{name}
%dir %{_sysconfdir}/pki/mock
%config(noreplace) %{_sysconfdir}/pki/mock/*
%{_mandir}/man1/mock.1*
%{_mandir}/man1/mock-parse-buildlog.1*
%{_mandir}/man1/mock-hermetic-repo.1*
%{_datadir}/cheat/mock

%files scm
%{python_sitelib}/mockbuild/scm.py*

%files lvm
%{python_sitelib}/mockbuild/plugins/lvm_root.*

%files rpmautospec
%{python_sitelib}/mockbuild/plugins/rpmautospec.*

%files filesystem
%license COPYING
%dir  %{_sysconfdir}/mock
%dir  %{_sysconfdir}/mock/eol
%dir  %{_sysconfdir}/mock/eol/templates
%dir  %{_sysconfdir}/mock/templates
%dir  %{_datadir}/cheat
%config(noreplace) %{_sysusersdir}/mock.conf

# cache & build dirs, writeable by mock group
%defattr(0775, root, mock, 0775)
%dir %{_localstatedir}/cache/mock
%dir %{_localstatedir}/lib/mock

%changelog
%autochangelog

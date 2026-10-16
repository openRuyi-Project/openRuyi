# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           packr2
%define go_import_path  github.com/gobuffalo/packr/v2

Name:           packr2
Version:        2.7.1
Release:        %autorelease
Summary:        Embed files in Go applications
License:        MIT AND BSD-2-Clause
URL:            https://github.com/gobuffalo/packr
#!RemoteAsset:  sha256:842bc86dfb34c1ff8d1cc1c12fb46cf30ad279eec17ecef8b122c151cfc16b85
Source0:        https://github.com/gobuffalo/packr/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang

# Legacy command help text fails the redundant-newline go vet check.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gobuffalo/envy)
BuildRequires:  go(github.com/gobuffalo/logger)
BuildRequires:  go(github.com/gobuffalo/packd)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

%package     -n go-github-gobuffalo-packr-v2
Summary:        Go source for packr2
BuildArch:      noarch

Provides:       go(github.com/gobuffalo/packr/v2) = %{version}

Requires:       go(github.com/gobuffalo/envy)
Requires:       go(github.com/gobuffalo/logger)
Requires:       go(github.com/gobuffalo/packd)
Requires:       go(github.com/rogpeppe/go-internal)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(github.com/spf13/cobra)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/tools)

%description
Embed files in Go applications.

%description -n go-github-gobuffalo-packr-v2
This package provides the reusable Go source for packr2.

%prep
%autosetup -C -p1
# Select the independently versioned v2 module from the monorepo archive.
find . -maxdepth 1 -mindepth 1 -not -name v2 -exec rm -rf {} +
shopt -s dotglob
mv v2/* .
rmdir v2
# Keep bundled license texts under distinct names.
mkdir licenses
cp LICENSE.txt licenses/packr-LICENSE
cp packr2/LICENSE licenses/packr2-LICENSE
cp internal/takeon/github.com/karrick/godirwalk/LICENSE licenses/godirwalk-LICENSE
for component in errx oncer safe; do
    cp internal/takeon/github.com/markbates/$component/LICENSE licenses/$component-LICENSE
done
%go_prep

%build
# The executable is below the library root.
%go_common
mkdir -p _bin
%{__go} build %{go_build_flags_default} -buildmode=pie -trimpath -o _bin/%{_name} %{go_import_path}/packr2

%install
install -D -m755 _bin/%{_name} %{buildroot}%{_bindir}/%{_name}
rm -rf _bin
%buildsystem_golangmodules_install

%check -a
%{buildroot}%{_bindir}/%{_name} version | grep -Fx "v%{version}"

%files
%doc README.md
%license licenses
%{_bindir}/%{_name}

%files -n go-github-gobuffalo-packr-v2
%doc README.md
%license licenses
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog

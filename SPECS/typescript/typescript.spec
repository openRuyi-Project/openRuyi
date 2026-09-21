# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           typescript
Version:        6.0.3
Release:        %autorelease
Summary:        TypeScript language compiler
License:        Apache-2.0
URL:            https://www.typescriptlang.org/
VCS:            git:https://github.com/microsoft/TypeScript.git
#!RemoteAsset:  sha256:33cd0ee1beaa8c9e9d15a9da836c62ddea4c34a42d7c2d349dbc80d94165d22a
Source0:        https://registry.npmjs.org/typescript/-/typescript-%{version}.tgz
BuildArch:      noarch

BuildRequires:  nodejs >= 14.17

Provides:       npm(typescript) = %{version}

Requires:       nodejs >= 14.17

%description
TypeScript is a language for application-scale JavaScript development.  This
package installs the official npm compiler distribution and command-line tools.

%prep
%autosetup -n package

%build
# The official npm tarball contains the already-built JavaScript compiler.

%install
install -d %{buildroot}%{_prefix}/lib/node_modules/typescript
cp -a bin lib %{buildroot}%{_prefix}/lib/node_modules/typescript/
install -pm 0644 package.json \
    %{buildroot}%{_prefix}/lib/node_modules/typescript/package.json

install -d %{buildroot}%{_bindir}
ln -s ../lib/node_modules/typescript/bin/tsc %{buildroot}%{_bindir}/tsc
ln -s ../lib/node_modules/typescript/bin/tsserver %{buildroot}%{_bindir}/tsserver

%check
node bin/tsc --version | grep -Fx 'Version %{version}'
node -e 'const ts = require("./lib/typescript.js"); if (ts.version !== "%{version}") process.exit(1)'

%files
%doc README.md SECURITY.md
%license LICENSE.txt ThirdPartyNoticeText.txt
%{_bindir}/tsc
%{_bindir}/tsserver
%dir %{_prefix}/lib/node_modules
%{_prefix}/lib/node_modules/typescript

%changelog
%autochangelog

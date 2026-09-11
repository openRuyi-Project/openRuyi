# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sarama
%define go_import_path  github.com/IBM/sarama
# Broker tests need a live Kafka cluster.
%define go_test_ignore_failure 1

Name:           go-github-ibm-sarama
Version:        1.45.1
Release:        %autorelease
Summary:        Go client for Apache Kafka
License:        MIT
URL:            https://github.com/IBM/sarama
#!RemoteAsset:  sha256:4e7cf2db71952e261c3076df830a15a95b42203aedca83f6bea5d64a32e85ab1
Source0:        https://github.com/IBM/sarama/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/eapache/go-resiliency)
BuildRequires:  go(github.com/eapache/go-xerial-snappy)
BuildRequires:  go(github.com/eapache/queue)
BuildRequires:  go(github.com/fortytw2/leaktest)
BuildRequires:  go(github.com/hashicorp/go-multierror)
BuildRequires:  go(github.com/jcmturner/gofork)
BuildRequires:  go(github.com/jcmturner/gokrb5/v8)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/pierrec/lz4/v4)
BuildRequires:  go(github.com/rcrowley/go-metrics)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/IBM/sarama) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/eapache/go-resiliency)
Requires:       go(github.com/eapache/go-xerial-snappy)
Requires:       go(github.com/eapache/queue)
Requires:       go(github.com/hashicorp/go-multierror)
Requires:       go(github.com/jcmturner/gofork)
Requires:       go(github.com/jcmturner/gokrb5/v8)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/pierrec/lz4/v4)
Requires:       go(github.com/rcrowley/go-metrics)
Requires:       go(golang.org/x/net)

%description
Sarama is a pure-Go client for Apache Kafka 0.8 and later. MinIO uses
it as a Kafka event-notification target.

%prep -a
# examples/ are sample programs with nested modules, not the library.
rm -rf examples
# tools/ holds kafka-console-* diagnostics and a performance client,
# not an upstream-distributed program. This RPM is the importable library.
rm -rf tools

%files
%doc README.md CHANGELOG.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           amqp091-go
%define go_import_path  github.com/rabbitmq/amqp091-go

Name:           go-github-rabbitmq-amqp091-go
Version:        1.10.0
Release:        %autorelease
Summary:        An AMQP 0-9-1 Go client maintained by the RabbitMQ team.
License:        BSD-2-Clause
URL:            https://github.com/rabbitmq/amqp091-go
#!RemoteAsset
Source0:        https://github.com/rabbitmq/amqp091-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(go.uber.org/goleak)

Provides:       go(github.com/rabbitmq/amqp091-go) = %{version}

%description
This is a Go AMQP 0.9.1 client maintained by the RabbitMQ core team.
It was originally developed by Sean Treadway.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog

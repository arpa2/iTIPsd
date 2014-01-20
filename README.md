# iTIPsd

> *The iTIPsd service implements the general iTIP protocol for exchange
> of iCalendar files almost directly, over bidirectionally authenticated
> TLS connections.*

This project delivers a daemon that listens for incoming iCalendar
submissions. Unlike CalDAV, it is suitable for realtime interactions,
and unlike iMIP (mail extensions) it does not require manual handling
(or accepting spam in your calendar).

The project is built on top of [TLS Pool][] for authentication, and uses
a general exchange layer for the actual data to be exchanged. Currently,
the exchanges are plain iCalendar messages over the TLS connection, but
we are considering to replace this with MSRP in a future version. That
future version will be incompatible with this one!

## Usefulness of MSRP

We are considering to run the iTIPsd as a special handling method for
MIME-type `text/calendar`, and use the MSRP protocol for exchanging it.
This means that many more document types can be transported with the
same protocol, and that it is even possible to negotiate about the
document types that are considered acceptable. MSRP is, in that sense,
comparable to HTTP.

The infrastructure of MSRP is normally defined as a method that is
negotiated in a contextual protocol, such as SIP/SDP, and it uses random
URL parts to define such end points. In order to break through NAT
and/or firewalls, there is an additional infrastructural component
called an MSRP Relay, through which the traffic can pass.

The MSRP Relay does not directly support URLs of the form
`msrp://user@domain.name` — so that these are still available for
connections which have not been agreed upon in a contextual protocol. It
is this URL format that we intend to use.

  [TLS Pool]: http://tlspool.org/
